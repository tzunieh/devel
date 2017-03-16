FROM zosimos/nodejs:latest

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rh/rh-ruby23/root/usr/lib64 \
    PATH=$PATH:/opt/rh/rh-ruby23/root/usr/bin:/opt/rh/rh-ruby23/root/usr/local/bin

RUN yum install -y vim gcc gcc-c++ \
    && yum install -y vim supervisor \
    && yum install -y make automake autoconf \
    && yum install -y curl-devel libcurl-devel openssl-devel zlib-devel httpd-devel apr-devel apr-util-devel \
    && yum install -y sqlite sqlite-devel libyaml \
    && yum install -y scl-utils \
    && yum install -y centos-release-scl \
    && yum install -y rh-ruby23 \
    && yum install -y rh-ruby23-ruby-devel \
    && source /opt/rh/rh-ruby23/enable \
    && gem install bundler \
    && gem install sass \
    && npm install babel-cli bower webpack forever gulp typescript gulp-util pretty-hrtime chalk semver archy liftoff tildify interpret v8flags minimist -g --save-dev

CMD ['bash']
