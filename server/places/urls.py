from django.conf.urls import url
from places import views

urlpatterns = [
    url(r'areas/$', views.AreaList.as_view()),
    url(r'areas/(?P<pk>[0-9]+)/$', views.AreaDetail.as_view()),
    url(r'attractions/$', views.AttractionList.as_view()),
    url(r'attractions/(?P<pk>\d+)/$', views.AttractionDetail.as_view()),
    url(r'attractions/in/(?P<pk>\d+)/$', views.area_attractions),
    url(r'attractions/nearby/(?P<lat>\d+\.\d+)/(?P<lon>\d+\.\d+)', views.attractions_nearby),
    url(r'hospitals/$', views.HospitalList.as_view()),
    url(r'hospitals/(?P<pk>\d+)/$', views.HospitalDetail.as_view()),
    url(r'hospitals/nearest/(?P<lat>\d+\.\d+)/(?P<lon>\d+\.\d+)', views.hospital_nearest)
]