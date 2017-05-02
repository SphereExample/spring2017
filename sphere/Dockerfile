FROM ubuntu:17.04

MAINTAINER Sergey Lihobabin <greyone@greyone.ru>

RUN groupadd -r sphere && useradd -r -g sphere sphere

RUN mkdir /opt/sphere
WORKDIR /opt/sphere

COPY requirements.txt /opt/sphere/requirements.txt

RUN apt-get update \
    && apt-get -yqq install libmysqlclient20 python3-pip python3-dev libmysqlclient-dev \
    && pip3 install -r /opt/sphere/requirements.txt --no-cache-dir \
    && apt-get remove python3-dev libmysqlclient-dev -y \
    && apt-get autoremove -y \
    && apt-get clean

COPY . /opt/sphere/

EXPOSE 5000

USER sphere

CMD ["gunicorn", "-w", "1", "--bind=0.0.0.0:5000", "application.wsgi:application"]
