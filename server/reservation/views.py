# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
from models import Call
from django.http import HttpResponse

# Create your views here.

DECLINE_XML = ['<?xml version="1.0" encoding="UTF-8"?> ' \
              '<Response>' \
              '<Say language="en-US"> You have declined the reservation. What a pity. You could earn money.</Say>' \
              '</Response>',

               '<?xml version="1.0" encoding="UTF-8"?> ' \
               '<Response>' \
               '<Say language="ja-JP"> わかりました。どうもありがとうございます。また、りようさせていただきます。</Say>' \
               '</Response>'
               ]

ACCEPT_XML = ['<?xml version="1.0" encoding="UTF-8"?> ' \
              '<Response>' \
              '<Say language="en-US"> You have accepted the reservation. Thank you very much.</Say>' \
              '</Response>',

              '<?xml version="1.0" encoding="UTF-8"?> ' \
              '<Response>' \
              '<Say language="ja-JP"> よやくしていただいて、どうもありがとうございました。どうぞよろしくおねがいします。</Say>' \
              '</Response>'
              ]

class XMLResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'text/xml; charset=utf-8'
        super(XMLResponse, self).__init__(data, **kwargs)

def XML_generate(pk):
    call_info = Call.objects.get(pk=pk)
    url = 'http://47.88.212.198:8000/gather/' + str(pk) + '/'
    num_people = call_info.num_people
    time = call_info.time
    date = call_info.date
    name = call_info.name
    language = call_info.language_opt

    if language == Call.JAPANESE:
        if num_people == 1:
            num_people_text = u'ひとり'
        elif num_people == 2:
            num_people_text = u'ふたり'
        else:
            num_people_text = num_people + u'人'

        xml = '<?xml version="1.0" encoding="UTF-8"?>' \
              '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}"> ' \
              '<Say language="ja-JP"> 私は、自動予約ロボットの、トージャです。今回は、{1}さんのかわりに予約しています。' \
              '{1}さんは、{2}、{3}時から、 {4}の予約をしたいです。' \
              '予約可能な場合は、１をおしてください。' \
              '予約出来ない場合は、２をおしてください。' \
              '、もう一度、聞き直す場合は、５を、おしてください' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>我々は、十分な情報が確認できませんでした。 またのご利用をお待ちしております！</Say> ' \
              '</Response>'.format(url, name, date, time, num_people_text)

    else:
        xml = '<?xml version="1.0" encoding="UTF-8"?>' \
              '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}"> ' \
              '<Say language="en-US"> Hi, this is an automated call from Toza. We want to reserve a table for {1} ' \
              'people at {2} {3}. The reservation is under the name of {4}... Again, the name is {4}...' \
              'Please press one to accept the reservation, press zero to decline! ' \
              'Or press 5 to listen to the message again.' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>We did not receive any input. Goodbye!</Say> ' \
              '</Response>'.format(url, num_people, time, date, name)

    return xml

def XML_generate_sorry(pk):
    call_info = Call.objects.get(pk=pk)
    url = 'http://47.88.212.198:8000/gather/' + str(pk) + '/'

    if call_info.language_opt == Call.JAPANESE:
        xml = '<Response> ' \
              '<Gather timeout="20" finishOnKey="" numDigits="1" method="GET" action="{0}">' \
              '<Say language="ja-JP"> あなたは間違った番号を選びました！もう一度お選びください。 ' \
              'よやくかのうなばあいは、１をおしてください。' \
              'よやくできないばあいは、２をおしてください。' \
              'もういちど、ききなおすばあいは、５をおしてください' \
              '</Say> ' \
              '</Gather> ' \
              '<Say>我々は、任意の入力を受信しませんでした。 さようなら！ </Say> ' \
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
    xml = XML_generate(pk = pk)
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
        xml = XML_generate(pk = pk)
    else:
        xml = XML_generate_sorry(pk = pk)

    response = XMLResponse(xml)

    return response

def twilio_call(request):
    account_sid = "AC9fd29fc278859337de38574c25843043"  # Your Account SID from www.twilio.com/console
    auth_token = "22388542078a89a05e264409a2ef0055"  # Your Auth Token from www.twilio.com/console

    name = request.GET.get('Name')
    num_people = request.GET.get('NPeople')
    date = request.GET.get('Date')
    time = request.GET.get('Time')
    #res_num = request.GET.get('ResNum')
    res_num = "+819071931989"

    if request.GET.get('Lang') == "en":
        language = Call.ENGLISH
    elif request.GET.get('Lang') == "ja":
        language = Call.JAPANESE
    else:
        language = Call.ENGLISH

    call_info = Call(name = name, num_people = num_people, date = date, time = time,
                     res_num = res_num, language_opt = language)
    call_info.save()
    # After save, I have this id.
    pk = call_info.pk
    url = "http://47.88.212.198:8000/reservation/" + str(pk) + '/'

    client = TwilioRestClient(account_sid, auth_token)

    try:
        call = client.calls.create(url=url,
                                   to=res_num,
                                   from_="+81345304650")
    except TwilioRestException as e:
        print(e)

    #print(call.account_sid)
    return HttpResponse("We are making the reservation call for you.")
