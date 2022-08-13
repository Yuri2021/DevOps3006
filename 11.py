import datetime # שימוש בפונקציה REQESTEST
from time import sleep
import requests
response = requests.get("https://github.com") # לינק לאתר
if response.status_code==200:
    print("git hub is up and running")
print(datetime.datetime.now()) # תאריך ושעה
sleep(10)
print(datetime.datetime.now())
