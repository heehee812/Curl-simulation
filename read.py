import time
import pycurl
from io import BytesIO 
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

# set up for line app
access_token= 'O8kuFrVBCMH6j4TcxbtKSqTWzzgBfejuvKgsn0yosH1CMb7g7NRZdJPorxOENF+y1GGKbx9+Km2Ffc4x/S/yPACFLtr9FveKo45X17kgDVfWmezJb8PNJ08JwZJc454oss6+fknmEssQskCs8tXTaQdB04t89/1O/w1cDnyilFU='
userId= 'U6b0f8d723a86579eda979e83510d36f1'
message= " "
line_bot_api = LineBotApi(access_token)
# set up for red file
filename= 'teraterms.log'
boom = 0
nowline = 0

# monitor the status if sensor
while True :
    fptr = open(filename)
    L = fptr.readlines()
    newline = len(L)
    for i in L[nowline:newline]:   
        print(i)
        if i[0] == '0':
            boom = 1
            break
    nowline = newline
    fptr.close()

    # call for help
    if boom == 1:
       help()
       break
    stop()

def help():
    get_location()
    send_message()

def get_location():
    b_obj = BytesIO() 
    crl = pycurl.Curl() 
    crl.setopt(crl.URL, 'https://ipinfo.io/json')
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform() 
    crl.close()
    get_body = b_obj.getvalue()
    message= get_body.decode('utf8')

def send_message():
        line_bot_api.push_message(userId, TextSendMessage(text='Crash.....(at a extend???), here is the location:'))
        line_bot_api.push_message(userId, TextSendMessage(text=message))
    
def stop():
    time.sleep(5)
    
