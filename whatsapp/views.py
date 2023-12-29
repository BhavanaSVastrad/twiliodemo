from django.shortcuts import HttpResponse
from twilio.rest import Client
from django.conf import settings

def send_whatsapp(request):
   
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
                              from_='whatsapp:' + settings.TWILIO_WHATSAPP_NUMBER,
                              body='Hello, there!',
                              to='whatsapp:+918951897993'
                          )

    return HttpResponse(f'WhatsApp message sent! SID: {message.sid}')
