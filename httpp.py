import pycurl
from io import BytesIO 

b_obj = BytesIO() 
crl = pycurl.Curl() 

# # Set URL value
# crl.setopt(crl.URL, 'https://charlyyxcnj.apps.exosite.io/get')

# # Write bytes that are utf-8 encoded
# crl.setopt(crl.WRITEDATA, b_obj)

# # Perform a file transfer 
# crl.perform() 

# # End curl session
# crl.close()

# # Get the content stored in the BytesIO object (in byte characters) 
# get_body = b_obj.getvalue()

# # Decode the bytes stored in get_body to HTML and print the result 
# print('Output of GET request:\n%s' % get_body.decode('utf8'))
# 

# Set URL value
crl.setopt(crl.URL, 'https://ipinfo.io/json')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request:\n%s' % get_body.decode('utf8')) 


# # line push message
# from linebot import LineBotApi
# from linebot.models import TextSendMessage
# from linebot.exceptions import LineBotApiError

# line_bot_api = LineBotApi('O8kuFrVBCMH6j4TcxbtKSqTWzzgBfejuvKgsn0yosH1CMb7g7NRZdJPorxOENF+y1GGKbx9+Km2Ffc4x/S/yPACFLtr9FveKo45X17kgDVfWmezJb8PNJ08JwZJc454oss6+fknmEssQskCs8tXTaQdB04t89/1O/w1cDnyilFU=')

# try:
#     line_bot_api.push_message('U6b0f8d723a86579eda979e83510d36f1', TextSendMessage(text='Hello World!'))
# except LineBotApiError as e:
#     pass

# location
