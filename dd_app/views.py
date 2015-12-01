from django.shortcuts import get_object_or_404, get_list_or_404, render
from django_tables2   import RequestConfig


from .models import Raceday, Race, Entry, EntryTable
from analyzer import calculate_scores

def index(request):
	latest_raceday_list = Raceday.objects.order_by('-date')[:5]
	context = {'latest_raceday_list': latest_raceday_list}
	return render(request, 'dd_app/index.html', context)

def races_list(request, raceday_id):
	races_list = get_list_or_404(Race, day=raceday_id)
	return render(request, 'dd_app/race_list.html', {'races_list':races_list})


def race_detail(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race_id)
	entries_with_scores = calculate_scores(entries)
	table = EntryTable(entries_with_scores)
	RequestConfig(request).configure(table)
	return render(request, 'dd_app/detail.html', {'table': table, 'race': race})

	# return render(request, 'dd_app/detail.html', 
	# 	{'race': race, 'scores': scores})	


