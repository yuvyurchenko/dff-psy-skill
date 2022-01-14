FROM python:3.8-slim

WORKDIR /app

# Install project dependencies
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Don't use terminal buffering, print all to stdout / err right away
ENV PYTHONUNBUFFERED 1

COPY ./config.yml ./config.yml
COPY ./nlu.yml ./data/nlu.yml

RUN rasa train nlu --fixed-model-name nlu.tar.gz

CMD rasa run --enable-api -m models/nlu.tar.gz

