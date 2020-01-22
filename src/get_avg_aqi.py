import requests
import json
import smtplib
from email.mime.text import MIMEText
import time

if __name__ == '__main__':

    url = 'http://www.pm25.in/api/querys/only_aqi.json?city=xian&token=5j1znBVAsnSf5xQyNQyq'
    RETRY = int(6)

    result = 999
    for retry_count in range(RETRY):
        if result == 200:
            break
        if retry_count >= RETRY:
            print('Get AQI info failed! Out of retry times')
            exit(1)
        try:
            retry_count = retry_count + 1
            respose = requests.get(url, verify=False)
            result =  respose.status_code
            print("Status Code: " + str(result))
        except:
            print('Get AQI failed. Retry Time: ' + str(retry_count))
            time.sleep(10)

    aqi_list = json.loads(respose.text)
    # print(json.dumps(respose.text))
    station_num = 0
    aqi_sum = 0
    for aqi_item in aqi_list:
        if aqi_item['aqi'] > 0:
            station_num += 1
            aqi_sum += aqi_item['aqi']

    avg_aqi = aqi_sum / station_num
    aqi_content = "The average AQI of Xi'an is " + str(avg_aqi)
    if avg_aqi >= 300:
        aqi_title = "Work from Home Day! [AQI: " + str(avg_aqi) + "]"
    else:
        aqi_title = "Need to Go to Work! [AQI: " + str(avg_aqi) + "]"
    print('avg_result: ' + aqi_content)

    # read email config
    config = json.load(open('config.json', 'r'))
    mail_host = config['mail_host']
    mail_user = config['mail_user']
    mail_password = config['mail_password']

    sender = mail_user
    receivers = config['receivers']

    content = aqi_content
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = aqi_title
    message['From'] = sender
    message['To'] = ','.join(receivers)

    print('message:\n' + message.as_string())

    # send email
    for retry_count in range(RETRY):
        if retry_count >= RETRY:
            print('Email Send failed! Out of retry times')
            exit(1)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(mail_user, mail_password)
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            smtpObj.quit()
            print('Email Send Successfully!')
            break
        except:
            print('Email Send failed! Try Again!')
            print('Retry Time: ' + str(retry_count))
            time.sleep(10)
