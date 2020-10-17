FROM python:3.7-alpine

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY . /app
WORKDIR /app

RUN apk update && apk add bash
RUN apk add --no-cache gcc \
    openssl-dev \
    libffi-dev \
    musl-dev \
    linux-headers \
    mariadb-connector-c-dev && \
    pip install -r requirements.txt

CMD ["/bin/bash"]
