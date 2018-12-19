FROM zosimos/python:latest
MAINTAINER "zosimos.pk@gmail.com"

ENV LD_LIBRARY_PATH=/usr/local/lib:$HOME/local/lib \
    LD_RUN_PATH=$LD_LIBRARY_PATH \
    PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib64/qt-3.3/bin

RUN pip3.7 install cmake \
 && pip3.7 install numpy \
 && pip3.7 install torch torchvision \
 && pip3.7 install jupyter \
 && pip3.7 install dlib \
 && pip3.7 install scikit-image \
 && pip3.7 install SymPy \
 && pip3.7 install matplotlib \
 && pip3.7 install Pillow \
 && pip3.7 install latex \
 && pip3.7 install ghostscript pdfebc \
 && pip3.7 install tox pytest \
 && pip3.7 install python-dateutil


CMD ['/bin/bash']
