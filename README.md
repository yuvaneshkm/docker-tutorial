# Docker Tutorial

# General commands:
### check docker installed or not:
```bash
docker
```
### version of the docker installed:
```bash
docker --version
```
### display system-wide information:
```bash
docker info
```
### start the docker daemon:
```bash
docker -d
```

# Commands related to docker images:
### build a docker image from dockerfile:
```bash
docker build -t <docker-image-name> .
```
### list all the local docker images:
```bash
docker images
```
### delete a docker image:
```bash
docker rmi <docker-image-name>
```
