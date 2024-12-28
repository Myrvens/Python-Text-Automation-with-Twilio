from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'  # Replace with your Account SID
auth_token = 'your_auth_token'    # Replace with your Auth Token
client = Client(account_sid, auth_token)

# Twilio phone number (purchased from Twilio)
twilio_phone_number = '+1234567890'  # Replace with your Twilio number

# Your personal phone number (recipient)
recipient_phone_number = ' your phone number ' 

# Send SMS
def send_message():
    message = client.messages.create(
        body="Hey, Good morning!",  # Message content
        from_=twilio_phone_number,  # Your Twilio phone number
        to=recipient_phone_number   # Recipient's phone number
    )
    print(f"Message sent! SID: {message.sid}")

send_message()
