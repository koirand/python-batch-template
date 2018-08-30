FROM python:3.6

LABEL maintainer "koirand <koirand.jp@gmail.com>"

RUN apt-get update && apt-get install -y \
    curl

RUN pip install \
    configparser \
    mysql-connector-python-rf

COPY . /batch

ENV ENV development
WORKDIR /batch
