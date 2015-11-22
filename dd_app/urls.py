from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	
	# ex: /raceday/3/
    url(r'^raceday/(?P<raceday_id>[0-9]+)/$', views.races_list, name='races_list'),

	# ex: /race/5/
    url(r'^race/(?P<race_id>[0-9]+)/$', views.race_detail, name='detail'),
]