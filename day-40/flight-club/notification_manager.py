from twilio.rest import Client

TWILIO_SID = "AC8aa391212c08e38a761de7f2292ea74c"
TWILIO_AUTH_TOKEN = "4125783e51aba7a4fb5e24f8bf595607"
TWILIO_VIRTUAL_NUMBER = "+16197366053"
TWILIO_VERIFIED_NUMBER = "+5511974880000"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)