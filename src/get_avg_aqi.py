import requests
import json

if __name__ == "__main__":

    url = 'http://www.pm25.in/api/querys/only_aqi.json?city=xian&token=5j1znBVAsnSf5xQyNQyq'

    try:
        respose = requests.get(url, verify=False)
    except :
        print("Get AQI info failed!")

    if respose.status_code != 200:
        raise Exception('Reture Code != 200.')

    aqi_list = json.loads(respose.text)
    print(json.dumps(respose.text))
    station_num = 0
    aqi_sum = 0
    for aqi_item in aqi_list:
        if aqi_item['aqi'] > 0:
            station_num += 1
            aqi_sum += aqi_item['aqi']

    print("The average AQI of Xi'an is " + str(aqi_sum/station_num))
