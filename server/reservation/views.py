from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class XMLResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'application/xhtml+xml'
        super(XMLResponse, self).__init__(data, **kwargs)

def reservation(request):

    if request.method == "GET":
        xml = '<Response> ' \
                '<Gather timeout="20" finishOnKey="*" method="GET" action="http://toja.larvafun.com/api/twilio/gather"> ' \
                    '<Say language="en-US"> Hi, this is an automated call from Toja. We want to reserve a table for two people at 7PM today. ' \
                                            'Please press one to accept the reservation, press zero to decline! Or press 5 to listen to the message again. ' \
                                            'Please finish with the star key. ' \
                    '</Say> ' \
                '</Gather> ' \
                '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

        response = XMLResponse(xml)
        return response

    return HttpResponse(status=400)

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
              '<Gather timeout="20" finishOnKey="*" method="GET" action="http://toja.larvafun.com/api/twilio/gather"> ' \
              '<Say language="en-US"> Hi, this is an automated call from Toja. We want to reserve a table for two people at 7PM today. ' \
              'Please press one to accept the reservation, press zero to decline! Or press 5 to listen to the message again. ' \
              'Please finish with the star key. ' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

    else:
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="*" method="GET" action="http://toja.larvafun.com/api/twilio/gather"> ' \
              '<Say language="en-US"> Sorry. You chose the wrong number! Please choose again. Number one to accept the reservation. ' \
              'Zero to decline the reservation. Or number 5 to listen to the reservation information again.' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'

    response = XMLResponse(xml)

    return response