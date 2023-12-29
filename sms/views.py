from django.shortcuts import HttpResponse
from twilio.rest import Client
from django.conf import settings

def send_sms(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body="Hi",
        from_=settings.TWILIO_PHONE_NUMBER,
        to="+918951897993"  # Replace with the desired phone number
    )

    return HttpResponse(f'SMS sent! SID: {message.sid}')
