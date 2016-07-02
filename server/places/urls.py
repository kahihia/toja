from django.conf.urls import url
from places import views

urlpatterns = [
    url(r'areas/$', views.area_list),
    url(r'areas/(?P<pk>[0-9]+)/$', views.area_detail),
    url(r'attractions/$', views.attraction_list),
    url(r'attractions/(?P<pk>\d+)/$', views.attraction_detail),
    url(r'attractions/in/(?P<pk>\d+)/$', views.area_attractions),
]