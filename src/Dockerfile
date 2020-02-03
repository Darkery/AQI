FROM python:3.7-alpine
RUN mkdir /project
WORKDIR /project

# Install cron
   RUN apk update && apk add \
        bash \
        libldap \
        gcc \
        libc-dev \
        python-dev \
        openldap-dev \
    && pip install --no-cache-dir python-ldap requests \
    && apk del \
        gcc \
        libc-dev \
        python-dev \
        openldap-dev \
    && rm -rf /tmp/*


COPY report_aqi.sh /project/
COPY get_avg_aqi.py /project/

RUN chmod +x /project/*

ENTRYPOINT /bin/bash
