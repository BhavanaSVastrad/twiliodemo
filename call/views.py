from django.shortcuts import HttpResponse
from twilio.rest import Client
from django.conf import settings

def make_call(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        to='+918951897993',  # Replace with the desired phone number
        from_=settings.TWILIO_PHONE_NUMBER,
        twiml='<Response><Say>Hi</Say></Response>'
    )

    return HttpResponse(f'Call initiated! SID: {call.sid}')
