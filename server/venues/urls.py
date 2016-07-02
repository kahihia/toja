from django.conf.urls import url
from venues import views

urlpatterns = [
    url(r'venues/$', views.venue_list),
    url(r'venues/(?P<pk>[0-9]+)/$', views.venue_detail),
    url(r'venues/loc/(?P<lat>\d+\.\d+)/(?P<lon>\d+\.\d+)/$', views.venue_nearby)
]