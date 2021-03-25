FROM ubuntu:16.04
MAINTAINER Verdado "oliversoh@gmail.com"
COPY ./requirements.txt /requirements.txt

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y python3.6 python3.6-dev python3-pip libjpeg-dev zlib1g-dev gcc musl-dev \
  && ln -sfn /usr/bin/python3.6 /usr/bin/python3 \
  && ln -sfn /usr/bin/python3 /usr/bin/python \
  && ln -sfn /usr/bin/pip3 /usr/bin/pip \
  && pip install --upgrade setuptools \
  && pip install --upgrade pip \
  && pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "-c", "while :; do sleep 10; done"]