FROM zosimos/python_node:latest

# http://tecadmin.net/install-ruby-2-2-on-centos-rhel/
# https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-on-centos-6-with-rvm
# https://www.softwarecollections.org/en/scls/rhscl/rh-ruby23/
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rh/rh-ruby23/root/usr/lib64 \
    PATH=$PATH:/opt/rh/rh-ruby23/root/usr/bin:/opt/rh/rh-ruby23/root/usr/local/bin \
    PYTHONPATH=/usr/local/lib/python3.6/site-packages

RUN yum install -y vim gcc gcc-c++; yum clean all \
    && yum install -y vim supervisor; yum clean all \
    && yum install -y make automake autoconf; yum clean all \
    && yum install -y curl-devel libcurl-devel openssl-devel zlib-devel httpd-devel apr-devel apr-util-devel; yum clean all \
    && yum install -y sqlite sqlite-devel libyaml; yum clean all \
    && yum install -y scl-utils; yum clean all \
    && yum install -y centos-release-scl; yum clean all \
    && yum install -y rh-ruby23; yum clean all \
    && yum install -y rh-ruby23-ruby-devel; yum clean all \
    && source /opt/rh/rh-ruby23/enable \
    && mkdir /var/log/supervisor \
    && which ruby \
    && gem install bundler \
    && gem install sass \
    && which sass \
    && pip3.6 install setuptools Django requests future -U \
    && npm install babel-cli bower webpack forever gulp gulp-util pretty-hrtime chalk semver archy liftoff tildify interpret v8flags minimist typescript tsd eslint http-server -g --save-dev

CMD ['bash']
