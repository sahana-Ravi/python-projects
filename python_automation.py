# pip install requests
# pip install schedule
import time
import schedule
import requests
mobile_number = ''


def send_message():
    resp = requests.post("http://textbelt.com/text", {
        'phone': "7892436133",
        'message': "Good Morning!",
        'key': 'textbelt'
    })
    print(resp.json())


schedule.every(10).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
