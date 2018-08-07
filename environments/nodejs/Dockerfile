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
    && curl --silent --location https://rpm.nodesource.com/setup_10.x | bash - \
    && yum -y install nodejs \
    && which node \
    && which npm


CMD ['/bin/bash']
