FROM python:3.8

WORKDIR /app

# Install project dependencies
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Don't use terminal buffering, print all to stdout / err right away
ENV PYTHONUNBUFFERED 1

COPY annotators annotators
COPY datastore datastore
COPY model model
COPY scenario scenario
COPY templates templates
COPY ./server.py ./server.py
COPY ./entrypoint.sh ./entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
