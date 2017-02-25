FROM centos:latest

ENV LD_LIBRARY_PATH=/usr/local/lib

RUN yum -y update \
    && yum install yum-utils -y \
    && yum-builddep python -y \
    && yum -y groupinstall "Development Tools" \
    && yum install gcc gcc-c++ -y \
    && yum install libffi-devel libxml2-devel libxslt-devel -y \
    && yum install openssl-devel -y \
    && yum install which cd screen wget tar gzip -y \
    && rm -rf /tmp/src \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && curl -O https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz \
    && tar xzvf Python-* \
    && cd Python-3.6.0 \
    && ./configure --enable-optimizations --enable-shared --with-system-expat --with-system-ffi \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src \
    && pip3.6 install requests -U \
    && python3.6 -c "print('Python has been installed successfully')"


CMD ['/bin/bash']
