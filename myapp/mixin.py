from django.conf import settings
from twilio.rest import Client

class MessageHandler:
    mobile_no = None
    otp = None

    def __init__(self,mobile_no, otp) -> None:
        self.mobile_no = mobile_no
        self.otp = otp

    def send_otp_on_mobile(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
            
            from_ = "+15044144805",
            body = f'your otp is {self.otp}',
            to= self.mobile_no
        )
        print('---',message)
        print(message.sid)