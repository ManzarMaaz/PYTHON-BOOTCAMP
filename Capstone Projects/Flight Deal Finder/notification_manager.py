from twilio.rest import Client

class NotificationManager:
    """
    Manages sending SMS notifications via the Twilio API.
    """
    def __init__(self, sid, auth_token, twilio_number, receiver_number):
        """
        Initializes the Twilio client using provided credentials.
        """
        self.client = Client(sid, auth_token)
        self.twilio_number = twilio_number
        self.receiver_number = receiver_number

    def send_sms(self, message_body: str):
        """
        Sends a text message with the specified body to the verified number.
        
        Args:
            message_body: The content of the SMS alert.
        """
        print("Sending SMS alert...")
        try:
            # Twilio API call to create the message
            message = self.client.messages.create(
                body=message_body,
                from_=self.twilio_number,
                to=self.receiver_number
            )
            print(f"SMS Status: {message.status}")
            print(f"SMS Body: {message.body}...\n")
        except Exception as e:
            # Catching and reporting any Twilio or general errors
            print(f"Failed to send SMS: {e}")
