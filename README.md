# Docker Tutorial

### Creating / Build a docker image:
```bash
docker build -t <docker-image-name> .
```

### List out all the docker images:
```bash
docker images
```

### Run the docker image inside a container:
```bash
docker run -d -p 5000:5000 <docker-image-name>
```

### Containers that are running:
```bash
docker ps
```

### Stop the container:
```bash
docker stop <CONTAINER ID>
```