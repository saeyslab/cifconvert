FROM python:3.6.7

RUN apt-get update
RUN apt-get install -y default-jdk
RUN pip install cifconvert

ENTRYPOINT ["cifconvert"]

