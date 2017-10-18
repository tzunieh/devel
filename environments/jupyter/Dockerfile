FROM zosimos/python36
MAINTAINER "zosimos.pk@gmail.com"


RUN yum -y update \
    && yum install yum-utils -y \
    && yum-builddep python -y \
    && yum -y groupinstall "Development Tools" \
    && yum install gcc gcc-c++ -y \
    && yum install libffi-devel libxml2-devel libxslt-devel -y \
    && yum install openssl-devel -y \
    && yum install -y centos-release-scl \
    && yum install -y devtoolset-4-gcc* \
    && scl enable devtoolset-4 bash \
    && gcc --version \
    && mkdir -p /opt/notebooks \
    && yum -y install epel-release redislite \
    && yum -y install gcc gcc-c++ python-pip python-devel atlas atlas-devel gcc-gfortran openssl-devel libffi-devel \
    && pip3.6 install -U virtualenv requests Pillow\
    && pip3.6 install -U numpy scipy wheel cryptography pandas nltk scikit-learn \
    && pip3.6 install -U mlpy matplotlib Theano \
    && pip3.6 install -U pydot-ng Pygments Sphinx nose \
    # && pip3.6 install -U https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp35-cp35m-linux_x86_64.whl \
    && pip3.6 install -U jupyter

ADD jupyter_config.py /root/.jupyter/jupyter_notebook_config.py

ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888

VOLUME /opt/notebooks

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
