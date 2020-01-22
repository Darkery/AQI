FROM python:3.7-alpine
RUN mkdir /project
WORKDIR /project

# Install cron
RUN apk update && apk add \
        bash \
        vim \
    && pip install --no-cache-dir python-ldap requests \
    && rm -rf /tmp/*


COPY entrypoint.sh /project/
COPY get_avg_aqi.py /project/
COPY config.json /project/

RUN chmod +x /project/*

ENTRYPOINT /bin/bash
