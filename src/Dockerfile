FROM ubuntu:16.04
RUN mkdir /project
WORKDIR /project

# Install cron
RUN apt-get update && apt-get install -y cron
RUN apt-get install -y vim

COPY . /project/

RUN chmod +x /project/*.sh

ENTRYPOINT /project/entrypoint.sh
