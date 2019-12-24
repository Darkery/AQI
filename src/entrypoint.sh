#!/bin/bash

# Start the run once job.
echo "Docker container has been started"

crontab /project/crontabfile

service cron start
