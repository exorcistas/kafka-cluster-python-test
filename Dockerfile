# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /producer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY producer.py producer.py
CMD [ "python3", "producer.py" ]