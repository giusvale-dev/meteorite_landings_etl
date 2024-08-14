"""
Main Script for Data Retrieval and Processing from NASA's Meteorite Landings API

Author: Giuseppe Valente <valentepeppe@gmail.com>

This script is responsible to manage the ETL process of the Meteorite Landings

Dependencies:
- threading: For managing concurrent threads.
- queue: For handling failed data retrieval ranges.
- Extractor: Custom class to handle data extraction from NASA's API.

Usage:
    python main.py
"""

from etl.extractor import Extractor
import threading
import queue

def recover_data(start_offset, end_offset, data_list, lock, failure_queue):
    """
    Retrieves data from a specified range of offsets using the Extractor class.

    Parameters:
    - start_offset (int): The starting offset for data retrieval.
    - end_offset (int): The ending offset for data retrieval.
    - data_list (list): A list to which the retrieved data will be appended.
    - lock (threading.Lock): A lock to synchronize access to data_list.
    - failure_queue (queue.Queue): A queue to store failed offset ranges.

    Returns:
    - None: The function does not return a value. It modifies data_list in-place
      and uses failure_queue to report errors.

    Side Effects:
    - Appends successfully retrieved data to data_list, using the provided lock
      for thread-safe operations.
    - Adds failed offset ranges to 
    """
from etl.extractor import Extractor
import threading
import queue

def recover_data(start_offset, end_offset, data_list, lock, failure_queue):
    """
    Retrieves data from a specified range of offsets using the Extractor class.

    This function attempts to fetch data in chunks of 1000 from the start_offset to the end_offset.
    If any errors occur during the data retrieval, the range that failed is put into the failure_queue
    for potential retry or logging.

    Parameters:
    - start_offset (int): The starting offset for data retrieval.
    - end_offset (int): The ending offset for data retrieval. Data retrieval stops if this offset is reached.
    - data_list (list): A list to which the retrieved data will be appended. This list is shared among threads.
    - lock (threading.Lock): A lock object used to synchronize access to the shared data_list, ensuring thread-safe modifications.
    - failure_queue (queue.Queue): A queue used to store the ranges of offsets where data retrieval failed. This allows for tracking and handling of errors.

    Returns:
    - None: This function does not return any value. It modifies data_list in-place and uses failure_queue to report errors.
    
    Side Effects:
    - Appends successfully retrieved data to the data_list, while maintaining thread safety using the provided lock.
    - Puts failed offset ranges into the failure_queue for further processing if an exception occurs.

    Exceptions:
    - Any exception raised during data retrieval is caught, and the corresponding range is added to the failure_queue.
    """
    extractor = Extractor()
    try:
        for i in range(start_offset, end_offset, 1000):
            print(f"Recovering 999 raw data from offset = {i}")
            tmp_data = extractor.get_data_from_nasa(i)
            if not tmp_data:
                break
            with lock:
                data_list.extend(tmp_data)
    except Exception as e:
        print(f"Error in range ({start_offset}, {end_offset}): {e}")
        failure_queue.put((start_offset, end_offset))

def main():
    num_threads = 5
    offsets = [(i * 10000, (i + 1) * 10000) for i in range(num_threads)]
    
    json_data = []
    lock = threading.Lock()
    failure_queue = queue.Queue()

    threads = []
    for start_offset, end_offset in offsets:
        thread = threading.Thread(target=recover_data, args=(start_offset, end_offset, json_data, lock, failure_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if failure_queue.empty():
        extractor = Extractor()
        print("Extraction completed")
    else:
        print("One or more threads failed. Reviewing failure details.")
        while not failure_queue.empty():
            failed_range = failure_queue.get()
            print(f"Failed range: {failed_range}")

if __name__ == "__main__":
    main()
