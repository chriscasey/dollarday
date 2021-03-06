from django.conf.urls import url

from . import views
from . import stats

urlpatterns = [
	url(r'^$', views.index, name='index'),
	
	# ex: /raceday/3/
    url(r'^raceday/(?P<raceday_id>[0-9]+)/$', views.races_list, name='races_list'),

	# ex: /race/5/
    url(r'^race/(?P<race_id>[0-9]+)/$', views.race_detail, name='detail'),
    
    # CHARTS
    # ex: /race/5/score_pie_chart
	url(r'^race/(?P<race_id>[0-9]+)/score_pie_chart', views.score_pie_chart, name='score_pie_chart'),
	# ex: /race/5/scatter_plot_graph
	url(r'^race/(?P<race_id>[0-9]+)/scatter_plot_graph', views.scatter_plot_graph, name='scatter_plot_graph'),
	# ex: /race/5/box_plot_chart
	url(r'^race/(?P<race_id>[0-9]+)/box_plot_chart', views.box_plot_chart, name='box_plot_chart'),
	# ex: /race/5/lifetime_win_bar_chart
	url(r'^race/(?P<race_id>[0-9]+)/lifetime_win_bar_chart', views.lifetime_win_bar_chart, name='lifetime_win_bar_chart'),
	# ex: /race/5/lifetime_win_grouped
	url(r'^race/(?P<race_id>[0-9]+)/lifetime_win_grouped', views.lifetime_win_grouped, name='lifetime_win_grouped'),
	# ex: /race/5/lifetime_win_bullet_chart
	url(r'^race/(?P<race_id>[0-9]+)/lifetime_win_bullet_chart', views.lifetime_win_bullet_chart, name='lifetime_win_bullet_chart'),
	# ex: /race/5/average_earnings_bullet_chart
	url(r'^race/(?P<race_id>[0-9]+)/average_earnings_bullet_chart', views.average_earnings_bullet_chart, name='average_earnings_bullet_chart'),

	# STATS
	# ex: /stats
	url(r'^stats', stats.results_all, name='results_all'),
	# ex: /stats/2015/
	url(r'^stats/(?P<year>[0-9]+)/$', stats.results_by_year, name='results_by_year'),
]