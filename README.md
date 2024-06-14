# Docker Tutorial


# General commands:
### Check docker installed or not:
```bash
docker
```
### Version of the docker installed:
```bash
docker --version
```
### Display system-wide information:
```bash
docker info
```
### Start the docker daemon:
```bash
docker -d
```


# Commands related to docker images:
### Build a docker image from dockerfile:
```bash
docker build -t <docker-image-name> .
```
### List all the local docker images:
```bash
docker images
```
### Delete a docker image:
```bash
docker rmi <docker-image-name>
```


# Commands related to docker containers:
### List all the containers that are running currently:
```bash
docker ps
```
### List all the containers running and stopped:
```bash
docker ps --all
```
### Run the docker container:
```bash
docker run -d -p <host-port>:<container-port> <docker-image-name>
```
### View resource usage stats:
```bash
docker container stats
```
### Stop the running container:
```bash
docker stop <CONTAINER ID>
```
