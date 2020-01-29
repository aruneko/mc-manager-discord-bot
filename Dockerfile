FROM python:3-alpine

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /usr/src/mc_manager

WORKDIR ${APP_HOME}

COPY requirements.txt .

RUN apk add --upgrade --virtual build-deps \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
 && pip install -r requirements.txt \
 && apk del build-deps

COPY manager_bot.py .

CMD [ "python", "./manager_bot.py" ]
