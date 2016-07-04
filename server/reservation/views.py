# coding=utf-8

import time
import pytz
import datetime

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from server.requests import JSONResponse

from models import Call
from venues.models import Venue
from serializers import CallSerializer

from server import secrets

DECLINE_XML = ['<?xml version="1.0" encoding="UTF-8"?> '
               '<Response>'
               '<Say language="en-US"> You have declined the reservation. What a pity. You could earn money.</Say>'
               '</Response>',

               '<?xml version="1.0" encoding="UTF-8"?> '
               '<Response>'
               u'<Say language="ja-JP"> 了解いたしました。ご確認ありがとうございます。また、予約がございましたら、'
               u'もう一度ご連絡させていただきます。</Say>'
               '</Response>'
               ]

ACCEPT_XML = ['<?xml version="1.0" encoding="UTF-8"?> '
              '<Response>'
              '<Say language="en-US"> You have accepted the reservation. Thank you very much.</Say>'
              '</Response>',

              '<?xml version="1.0" encoding="UTF-8"?> '
              '<Response>'
              u'<Say language="ja-JP"> よやくしていただいて、どうもありがとうございました。どうぞよろしくおねがいします。</Say>'
              '</Response>'
              ]


class XMLResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'text/xml; charset=utf-8'
        super(XMLResponse, self).__init__(data, **kwargs)


def xml_generate(pk):

    call_info = Call.objects.get(pk=pk)
    url = 'http://tjr.tonny.me/gather/' + str(pk) + '/'
    num_people = call_info.num_people
    dt = call_info.date_time
    tz = pytz.timezone('Asia/Tokyo')
    dt = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()),tz=tz)

    name = call_info.name
    language = call_info.language_opt

    # Using datetime field.
    # How does the Japanese deal with the date formatting?
    month = dt.strftime('%m').lstrip('0')
    day = dt.strftime('%d').lstrip('0')
    hour = dt.strftime('%H').lstrip('0')
    minute = dt.strftime('%M').lstrip('0')

    date_res = dt.date()
    date_now = datetime.datetime.now().date()

    cus_phone = call_info.cus_phone
    cus_phone = ". ".join(cus_phone)

    if language == Call.JAPANESE:
        if num_people == 1:
            num_people_text = u'ひとり'
        elif num_people == 2:
            num_people_text = u'ふたり'
        else:
            num_people_text = num_people + u'人'

        message_datetime = month + u'月' + day + u'日' + hour + u'時' + minute + u'分'
        # Check if today or tomorrow or other date
        if date_res == date_now:
            message_datetime == u'今日'+ message_datetime
        elif date_res == (date_now + datetime.timedelta(days=1)):
            message_datetime == u'明日'+ message_datetime

        xml = '<?xml version="1.0" encoding="UTF-8"?>' \
              '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}"> ' \
              u'<Say language="ja-JP"> 私は、自動予約ロボットの、トージャです。今回は、{1}さんのかわりに予約しています。' \
              u'{1}さんは、{2}から、 {3}の予約をしたいです。連絡電話番号は. {4}です。' \
              u'繰り返します。連絡電話番号は{4}です。' \
              u'予約可能な場合は、１をおしてください。' \
              u'予約出来ない場合は、２をおしてください。' \
              u'、もう一度、聞き直す場合は、５を、おしてください' \
              '</Say> ' \
              '</Gather> ' \
              u'<Say>我々は、十分な情報が確認できませんでした。 またのご利用をお待ちしております！</Say> ' \
              '</Response>'.format(url, name, message_datetime, num_people_text, cus_phone)

    else:

        if num_people == 1:
            num_people_text = '1 person'
        else:
            num_people_text = str(num_people) + ' people'

        month_text = dt.strftime("%B")
        if day == '1' or day == '21':
            day = day + 'st'
        elif day == '2' or day == '22':
            day = day + 'nd'
        elif day == '3' or day == '23':
            day = day + 'rd'
        else:
            day = day + 'th'

        message_datetime = month_text + ' ' + day + ' at ' + hour + ' o\'clock and ' + minute + ' minutes '
        # Check if today or tomorrow or other date
        if date_res == date_now:
            message_datetime == 'today' + message_datetime
        elif date_res == (date_now +  datetime.timedelta(days=1)):
            message_datetime == 'tomorrow' + message_datetime
        else:
            message_datetime == 'on' + message_datetime
        xml = '<?xml version="1.0" encoding="UTF-8"?>' \
              '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}"> ' \
              '<Say language="en-US"> Hi, this is an automated call from Toza. We want to reserve a table for {1} ' \
              '{2}. The reservation is under the name of {3}... The phone number of {3} is {4}...' \
              'Please press one to accept the reservation, press zero to decline! ' \
              'Or press 5 to listen to the message again.' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'.format(url, num_people_text, message_datetime, name, cus_phone)

    return xml


def xml_generate_sorry(pk):
    call_info = Call.objects.get(pk=pk)
    url = 'http://tjr.tonny.me/gather/' + str(pk) + '/'

    if call_info.language_opt == Call.JAPANESE:
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}">' \
              u'<Say language="ja-JP"> もう一度正しい番号をお選びください！ ' \
              u'よやくかのうなばあいは、１をおしてください。' \
              u'よやくできないばあいは、２をおしてください。' \
              u'もういちど、ききなおしたいばあいは、５をおしてください' \
              '</Say> ' \
              '</Gather> ' \
              u'<Say>我々は、任意の入力を受信しませんでした。 さようなら！ </Say> ' \
              '</Response>'.format(url)
    else:
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}">' \
              '<Say language="en-US"> Sorry. You chose the wrong number! Please choose again. ' \
              'Number one to accept the reservation. ' \
              'Zero to decline the reservation. Or number 5 to listen to the reservation information again.' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'.format(url)

    return xml


@csrf_exempt
def reservation(request, pk):
    xml = xml_generate(pk=pk)
    if request.method == "POST":
        call_info = Call.objects.get(pk=pk)
        call_info.status = Call.ON_CALLING
        call_info.save()
        response = XMLResponse(xml)
        return response

    return HttpResponse("Reservation info will only be shown by POST request.")


def gather(request, pk):
    call_info = Call.objects.get(pk=pk)
    digit = request.GET.get('Digits')

    if digit == '1':
        xml = ACCEPT_XML[call_info.language_opt]
        call_info.status = Call.ACCEPTED
        call_info.save()
    elif digit == '0':
        xml = DECLINE_XML[call_info.language_opt]
        call_info.status = Call.DECLINED
        call_info.save()
    elif digit == '5':
        xml = xml_generate(pk=pk)
    else:
        xml = xml_generate_sorry(pk=pk)

    response = XMLResponse(xml)
    return response


def twilio_call(request):

#    if request.method is not 'GET':
#        return HttpResponse(status=400)


    account_sid = secrets.TWILIO_ACCOUNT_SID  # Your Account SID from www.twilio.com/console
    auth_token = secrets.TWILIO_ACCOUNT_SECRET  # Your Auth Token from www.twilio.com/console

    required = ['name', 'npeople', 'datetime', 'resid', 'cusphone', 'lang']
    for req in required:
        if req not in request.GET:
            return JSONResponse(status=400)

    name = request.GET.get('name')
    num_people = request.GET.get('npeople')
    timestamp = request.GET.get('datetime')
    jptz = pytz.timezone('Asia/Tokyo')
    dt = datetime.datetime.fromtimestamp(float(timestamp), tz=jptz)
    shopid = request.GET.get('resid')
    if request.GET.get('lang') == "ja":
        language = Call.JAPANESE
    else:
        language = Call.ENGLISH
    cus_phone = request.GET.get('cusphone')

    shop_info = Venue.objects.get(pk = shopid)
    #res_phone = shop_info.phone
    res_phone = secrets.TEST_PHONE
    res_name = shop_info.name

    call_info = Call()
    call_info.name = name
    call_info.num_people = num_people
    call_info.date_time = dt
    call_info.res_phone = res_phone
    call_info.cus_phone = cus_phone
    call_info.language_opt = language
    call_info.res_name = res_name
    call_info.save()

    # After save, I have this id.
    pk = call_info.pk

    # Make request to Twilio.
    url = "http://tjr.tonny.me/reservation/" + str(pk) + '/'
    client = TwilioRestClient(account_sid, auth_token)

    try:
        call = client.calls.create(url=url, to=res_phone, from_=secrets.TWILIO_PHONE,
                                   status_callback="http://tjr.tonny.me/callingstatus/" + str(pk) + '/',
                                   status_callback_method="POST",
                                   )
    except TwilioRestException as e:
        print(e)

    serializer = CallSerializer(call_info)
    return JSONResponse(serializer.data)
    # return HttpResponse("We are making the reservation call for you.")


class CallDetail(generics.RetrieveAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


@csrf_exempt
def check_status(request, pk):

    if request.method != 'GET':
        return HttpResponse(status=403)

    try:
        call = Call.objects.get(pk=pk)
    except Call.DoesNotExist:
        return HttpResponse(status=404)

    status = {call.status: Call.STATUS_CHOICES[call.status]}
    return JSONResponse(status)

@csrf_exempt
def get_twilio_call_status(request, pk):
    call_info = Call.objects.get(pk=pk)
    status = request.POST.get('CallStatus')
    if status == 'completed' and call_info.status == Call.ON_CALLING:
        call_info.status = Call.FAILED
    elif status in ['busy', 'failed', 'no-answer', 'canceled']:
        call_info.status = Call.FAILED
    elif status in ['ringing', 'in-progress']:
        call_info.status = Call.ON_CALLING
    elif status == 'queued':
        call_info.status = Call.READY
    call_info.save()
    serializer = CallSerializer(call_info)
    return JSONResponse(serializer.data)