import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACe86c64401253b9401e5eed67594c5576"
auth_token = "12074907b044ff5a9a1d83998aaf8abe"
client = Client(account_sid, auth_token)
print(client)


message = client.messages \
                .create(
                     body="Kaboom Abra Mining",
                     from_='+17147063423',
                     to='+639362403697'
                 )

print(message.sid)
print(message.status)
