import os
from twilio.rest import Client

account_sid='AC05184e1041040a42eb40034eae15dbee'
auth_token='7761960f3624cb918515393b9ca50dae'

client = Client(account_sid,auth_token)
message = client.messages.create(
body ="test bot",
from_ ='whatsapp:+6287888896864',
to ='whatsapp:6287776584079')

print (message.sid)
print("message sent")