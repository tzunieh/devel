FROM golang:latest

RUN apt-get update && \
    apt-get install libstemmer-dev -y


ENV GOPATH=/go \
    PATH=$PATH:$GOPATH/bin


CMD ['/bin/bash']
