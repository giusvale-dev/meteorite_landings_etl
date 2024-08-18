#!/bin/bash
#Clean all docker images
docker compose down --rmi all --volumes --remove-orphans
docker system prune -a