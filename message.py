
from twilio.rest import Client

def send_sms(content):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC84fe5428771daecc12bde1c241e6191e'
    auth_token = 'f80567c77a1aa7280f5b858d4c8c1972'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=content,
                         from_='+14758897767',
                         to='+14168326682'
                     )

    print(message.sid)
