FROM centos:latest

ENV LD_LIBRARY_PATH=/usr/local/lib:$HOME/local/lib \
    LD_RUN_PATH=$LD_LIBRARY_PATH

RUN yum -y update \
    && yum install yum-utils -y \
    && yum-builddep python -y \
    && yum -y groupinstall "Development Tools" \
    && yum install gcc gcc-c++ -y \
    && yum install libffi-devel libxml2-devel libxslt-devel -y \
    && yum install openssl-devel -y \
    # for fixing Delta RPMs disabled because /usr/bin/applydeltarpm not installed. error
    && yum install deltarpm -y \
    && yum install which cd screen wget tar gzip -y \
    && rm -rf /tmp/src \
    && echo "------------------------- Install Python 3.5.3 --------------------------" \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && curl -O https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz \
    && tar xzvf Python-* \
    && cd Python-3.5.3 \
    && ./configure --enable-optimizations --enable-shared --with-system-expat --with-system-ffi \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src \
    && /usr/local/bin/pip3.5 install requests -U \
    && /usr/local/bin/python3.5 -c "print('Python has been installed successfully')"


CMD ['/bin/bash']
