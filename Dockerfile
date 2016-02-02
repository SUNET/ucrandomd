FROM ubuntu
MAINTAINER leifj@sunet.se
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -q update
RUN apt-get install -y python python-virtualenv
RUN pip install setuptools
COPY . /usr/src/ucrandomd
WORKDIR /usr/src/ucrandomd
RUN python setup.py install
COPY entrypoint.sh /entrypoint.sh
RUN chmod a+rx /entrypoint.sh
EXPOSE 4711
ENTRYPOINT ["/entrypoint.sh"]
