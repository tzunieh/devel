FROM zosimos/python35:latest

RUN rm -rf /tmp/src \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && wget http://nodejs.org/dist/latest-v7.x/node-v7.9.0.tar.gz \
    && tar xzvf node-v* \
    && cd ./node-v7.9.0 \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm -rf /tmp/src

CMD ['/bin/bash']
