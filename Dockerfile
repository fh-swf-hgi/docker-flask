FROM ubuntu:18.04
MAINTAINER Heiner Giefers "giefers.heiner@fh-swf.de"

RUN apt-get update ; \
  apt-get install -y python python-pip ; \
  apt-get clean
RUN pip install --no-cache-dir Flask

ADD app.py /home/app.py

EXPOSE 5000
WORKDIR /home
CMD ["python", "app.py"]
