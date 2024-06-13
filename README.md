# Docker Tutorial

### Creating / Build a docker image:
```bash
docker build -t docker-tutorial .
```

### Creating a container
```bash
docker run -d -p 5000:5000 docker-tutorial
```