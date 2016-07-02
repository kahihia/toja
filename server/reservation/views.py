from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

class XMLResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'text/xml; charset=utf-8'
        super(XMLResponse, self).__init__(data, **kwargs)

@csrf_exempt
def reservation(request):

    if request.method == "POST":
        xml = '<Response> ' \
                '<Gather timeout="20" finishOnKey="" numDigits=1 method="GET" action="http://47.88.212.198:8000/gather/"> ' \
                    '<Say language="en-US"> Hi, this is an automated call from Toja. We want to reserve a table for two people at 7PM today. ' \
                                            'Please press one to accept the reservation, press zero to decline! Or press 5 to listen to the message again. ' \
                                            'Please finish with the star key. ' \
                    '</Say> ' \
                '</Gather> ' \
                '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

        response = XMLResponse(xml)
        return response

    return HttpResponse("Reservation info will only be shown by POST request.")

def gather(request):

    digit = request.GET.get('Digits')
    if digit == '1':
        xml = '<?xml version="1.0" encoding="UTF-8"?> ' \
              '<Response>' \
                    '<Say> You have accepted the reservation. Thank you very much.</Say>' \
              '</Response>'


    elif digit == '0':
        xml = '<?xml version="1.0" encoding="UTF-8"?> ' \
              '<Response>' \
                    '<Say> You have declined the reservation. Thank you very much.</Say>' \
              '</Response>'

    elif digit == '5':
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits=1 method="GET" action="http://47.88.212.198:8000/gather/"> ' \
              '<Say language="en-US"> Hi, this is an automated call from Toja. We want to reserve a table for two people at 7PM today. ' \
              'Please press one to accept the reservation, press zero to decline! Or press 5 to listen to the message again. ' \
              'Please finish with the star key. ' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

    else:
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits=1 method="GET" action="http://47.88.212.198:8000/gather/"> ' \
              '<Say language="en-US"> Sorry. You chose the wrong number! Please choose again. Number one to accept the reservation. ' \
              'Zero to decline the reservation. Or number 5 to listen to the reservation information again.' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

    response = XMLResponse(xml)

    return response

def twilio_call(request):
    from twilio import TwilioRestException
    from twilio.rest import TwilioRestClient

    account_sid = "AC9fd29fc278859337de38574c25843043"  # Your Account SID from www.twilio.com/console
    auth_token = "22388542078a89a05e264409a2ef0055"  # Your Auth Token from www.twilio.com/console

    client = TwilioRestClient(account_sid, auth_token)

    try:
        call = client.calls.create(url="http://47.88.212.198:8000/reservation/",
                                   to="+819071931989",
                                   from_="+81345304650")
    except TwilioRestException as e:
        print(e)

    print(call.account_sid)
    return HttpResponse("We are making the reservation call for you.")
