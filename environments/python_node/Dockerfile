FROM zosimos/python36:latest

RUN rm -rf /tmp/src \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && wget https://nodejs.org/dist/v8.7.0/node-v8.7.0.tar.gz \
    && tar xzvf node-v* \
    && cd ./node-v8.7.0 \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src

CMD ['/bin/bash']
