# Setup Golang Development Environment

## Using Docker
If you haven't install Docker in your Mac, please download from [here](https://www.docker.com/).

Once you have Docker installed, you will need to build a base Docker image first.

```bash
$ cd environment/golang
$ docker build -t golang .
```

What we are doing in here is we use `docker build` to build a reuseable base docker image `golang:latest` from our `Dockerfile`. This will be the base image when everytime you want to spin up a new container for your Python36 on Linux development.


With the base image we just created, we can now spin up a new container for my Python development.

```bash
$ docker run --name go_dev -p 8090:8090 -v $PWD:/go -it golang:latest bash
```

Above command will create a news Docker container then mount the current directory `$PWD` to `/go` inside of your Docker environment, so youc can easily sync up your code change between your Docker and Host(Mac) environment.

After exected this command, you should be able to see the new environment you just created. Let's exit and stop docker container first.

```bash
$ exit
```

Use this command to check the **running** container. 

```bash
$ docker ps
```

If you can't see anything, it's because your container just stopped by you. `docker ps` will only give you the list of running containers. To see **ALL** containers, you need to add `-al` param.

```bash
$ docker ps -al
```

Now you should be able to see your docker container:

```bash
$ docker ps -al
CONTAINER ID        IMAGE             COMMAND             CREATED             STATUS              PORTS                    NAMES
e7165993e2e7        golang:latest     "bash"              9 hours ago         Up 39 minutes       0.0.0.0:4080->4080/tcp   <YourContainerName>
```

To **start** and **access** your container when everytime you want to work on your development, you just need to execute this command:

```bash
$ docker start <YourContainerName> && docker exec -it <YourContainerName> bash
```

### Clean Up Docker Containers
After finished your development or messed up with your environment, you might want to clean up those useless Docker containers. 


#### Remove Single Container
```bash
$ docker stop <ContainerID>
$ docker rm <ContainerID>
```

#### Remove All Containers (No matter it's running or not)

```bash
$ docker stop $(docker ps -a -q)
$ docker rm $(docker ps -a -q)
```

### Remove Docker Image
Before removing image, you will need to make sure that you remove all containers which was built from this image.

List all Docker images

```bash
$ docker images
REPOSITORY     TAG           IMAGE ID            CREATED             SIZE
golang         latest        db6728504976        9 hours ago         3.61 GB
```


Delete Docker Images

```bash
$ docker rmi <IMAGE ID>
```