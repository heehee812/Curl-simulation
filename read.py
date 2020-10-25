import time
import pycurl
from io import BytesIO
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
#get location and push api
access_token= 'O8kuFrVBCMH6j4TcxbtKSqTWzzgBfejuvKgsn0yosH1CMb7g7NRZdJPorxOENF+y1GGKbx9+Km2Ffc4x/S/yPACFLtr9FveKo45X17kgDVfWmezJb8PNJ08JwZJc454oss6+fknmEssQskCs8tXTaQdB04t89/1O/w1cDnyilFU='
userId= 'U6b0f8d723a86579eda979e83510d36f1'
text=['mild impact..., here is the location:',
      'impact! here is the location:',
      'severe impact!!! here is the location:']

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
    return message.split(':')[6].split(',')[0:2]

def send_message(message,t):
    try:
        url= 'https://www.google.com/maps/search/?api=1&query='+ message
        line_bot_api.push_message(userId, TextSendMessage(text=t))
        line_bot_api.push_message(userId, TextSendMessage(text=url))
    except LineBotApiError as e:
        pass
   
def call(i):
    m= get_location()
    send_message(','.join(m[:])[2:-1],text[i-1])
   
def stop():
    time.sleep(5)
print(boom)

while True :
    fptr = open("teraterm.txt")
    L = fptr.readlines()
    newline = len(L)
    for i in L[nowline:newline]:
        print(i)
        if i[0] == '1':
            boom = 1
            break;    
        elif i[0] == '2':
            boom = 2
            break;
        elif i[0] == '3':
            boom = 3
            break;    
        else:
            pass
    nowline = newline
    fptr.close()
   
    if boom != 0:
       call(boom)
       break

    stop()