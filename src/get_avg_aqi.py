import requests
import json
import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':

    url = 'http://www.pm25.in/api/querys/only_aqi.json?city=xian&token=5j1znBVAsnSf5xQyNQyq'

    try:
        respose = requests.get(url, verify=False)
    except :
        print('Get AQI info failed!')

    if respose.status_code != 200:
        raise Exception('Reture Code != 200.')

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
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_password)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        print('Email Send Success!')
    except smtplib.SMTPException as e:
        print('Error', e)
        exit(1)
