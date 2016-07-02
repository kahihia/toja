from django.conf.urls import url

from . import views

urlpatterns = [

    #
    url(r'reservation/(?P<pk>[0-9]+)/', views.reservation),
    url(r'gather/(?P<pk>[0-9]+)/', views.gather),

    # Takes query as post.
    url(r'call/$', views.twilio_call),

    # Detail view of call.
    url(r'call/(?P<pk>\d+)/$', views.call_detail),

    # Check status of reservation/call.
    url(r'call/status/(?P<pk>\d+)/$', views.check_status),
]
