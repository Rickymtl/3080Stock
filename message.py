
from twilio.rest import Client

def send_sms(content):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=content,
                         from_='+14758897767',
                         to='+14168326682'
                     )

    print(message.sid)
