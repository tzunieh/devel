FROM centos:latest
MAINTAINER "zosimos.pk@gmail.com"

ENV LD_LIBRARY_PATH=/usr/local/lib:$HOME/local/lib \
    LD_RUN_PATH=$LD_LIBRARY_PATH \
    PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib64/qt-3.3/bin

RUN yum -y update \
    && yum install yum-utils -y; yum clean all \
    && yum-builddep python -y; yum clean all \
    && yum -y groupinstall "Development Tools" \
    && yum install gcc gcc-c++ -y; yum clean all \
    && yum install libffi-devel libxml2-devel libxslt-devel -y; yum clean all \
    && yum install openssl-devel -y; yum clean all \
    && yum install deltarpm -y; yum clean all \
    && yum install which cd screen wget tar gzip -y; yum clean all \
    && rm -rf /tmp/src \
    && echo "------------------------- Install Python 3.7.1 --------------------------" \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && curl -O https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz \
    && tar xzvf Python-* \
    && cd Python-3.7.1 \
    && ./configure --enable-optimizations --enable-shared --with-system-expat --with-system-ffi \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src \
    && pip3.7 install --upgrade pip setuptools \
    && pip3.7 install --upgrade requests \
    && pip3.7 install redislite \
    && pip3.7 install confset>=0.0.66 \
    && pip3.7 install ansible \
    && pip3.7 install hatch poetry \
    && pip3.7 install bottle \
    && pip3.7 install networkx \
    && pip3.7 install gitpython \
    && pip3.7 install cffi \
    && python3.7 -c "print('Python has been installed successfully')"


CMD ['/bin/bash']
