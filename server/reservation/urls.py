from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'reservation/(?P<pk>[0-9]+)/', views.reservation),
    url(r'gather/(?P<pk>[0-9]+)/', views.gather),
    url(r'call/', views.twilio_call)
]