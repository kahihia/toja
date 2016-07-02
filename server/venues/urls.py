from django.conf.urls import url
from venues import views

urlpatterns = [
    url(r'venues/$', views.VenueList.as_view()),
    url(r'venues/(?P<pk>[0-9]+)/$', views.VenueDetail.as_view()),
    url(r'venues/loc/(?P<lat>\d+\.\d+)/(?P<lon>\d+\.\d+)/$', views.venue_nearby),
    url(r'categories/$', views.CategoryList.as_view()),
    url(r'categories/(?P<pk>\d+)/$', views.category_venues),
]