#!/bin/bash

# Start the run once job.
echo "Start to get AQI info. Please wait."

python get_avg_aqi.py

if [ $? -eq 0 ];then
    echo "Send Report successfully."
else
    echo "Send Report unsuccessfully."
fi
