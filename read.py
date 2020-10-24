import time
import pycurl
from io import BytesIO
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
#get location and push api
access_token= 'O8kuFrVBCMH6j4TcxbtKSqTWzzgBfejuvKgsn0yosH1CMb7g7NRZdJPorxOENF+y1GGKbx9+Km2Ffc4x/S/yPACFLtr9FveKo45X17kgDVfWmezJb8PNJ08JwZJc454oss6+fknmEssQskCs8tXTaQdB04t89/1O/w1cDnyilFU='
userId= 'U6b0f8d723a86579eda979e83510d36f1'
line_bot_api = LineBotApi(access_token)
b_obj = BytesIO()
crl = pycurl.Curl()
#read file
boom = 0
nowline = 0
   
def get_location():
    # Set URL value
    crl.setopt(crl.URL, 'https://ipinfo.io/json')
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    message= get_body.decode('utf8')
    print('Output of GET request:\n%s' % message)
    return message

def send_message(message):
    try:
        line_bot_api.push_message(userId, TextSendMessage(text='Crash.....(at a extend???), here is the location:'))
        line_bot_api.push_message(userId, TextSendMessage(text=message))
    except LineBotApiError as e:
        pass
   
def call():
    m= get_location()
    send_message(m)
   
def stop():
    time.sleep(5)

while True :
    fptr = open("teraterm.txt")
    L = fptr.readlines()
    newline = len(L)
    for i in L[nowline:newline]:
        print(i)
        if i[0] == '0':
            boom = 1
            break;      
    nowline = newline
    fptr.close()
    if boom == 1:
       call()
       break
    stop()
