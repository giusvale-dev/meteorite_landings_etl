# Meteorite Landings ETL

This project is designed to extract, transform, and load meteorite landing data. The project is structured to be easily manageable, with a focus on modularity and maintainability.

## Project Structure

- `main.py`: The entry point for the ETL process.
- `models/`: Contains data models.
- `orm/`: Contains database mappings using an ORM.
- `requirements.txt`: Project dependencies.
- `Dockerfile`: Docker configuration file for containerization.
- `docker-compose.yml`: Docker Compose file to run the application in a container.
- `README.md`: This file.

## Development Setup (Using Virtual Environment)

For local development, it’s recommended to use a Python virtual environment (`venv`):

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:giusvale-dev/meteorite_landings_etl.git
cd meteorite_landings_etl
```
### 2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Running the ETL process locally:

```bash
python main.py
```
### 4. Deactivating the Virtual Environment

```bash
deactivate
```
## Development Setup (Using Docker)
If you want to build on Docker:

### 1. Build the docker image
```bash
docker-compose build
```

### 1. Run the docker image
```bash
docker-compose up
```

## Contact
For any inquiries or support, please contact valentepeppe@gmail.com
