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
