# Docker Image: zosimos/python


## Login docker hub

```bash
$ docker login --username=zosimos
```

## Build and push docker image to Docker hub

```bash
$ docker build -t zosimos/python_ml_dev:latest .
$ docker push zosimos/python_ml_dev:latest
```

```bash
$ docker run \
    --name ml_dev \
    -p 8882:4080 \
    -v $PWD:/home/projects \
    --privileged -it zosimos/python_ml_dev:latest bash
```
