FROM centos:latest

ENV LD_LIBRARY_PATH=/usr/local/lib

RUN yum -y update \
    && yum install yum-utils -y \
    && yum -y groupinstall "Development Tools" \
    && yum install gcc gcc-c++ -y \
    && yum install libffi-devel libxml2-devel libxslt-devel -y \
    && yum install openssl-devel -y \
    && yum install which cd screen wget tar gzip -y \
    && rm -rf /tmp/src \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && wget http://nodejs.org/dist/latest-v7.x/node-v7.7.3.tar.gz \
    && tar xzvf node-v* \
    && cd ./node-v7.7.3 \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src

CMD ['/bin/bash']