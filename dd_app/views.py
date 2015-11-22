from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Raceday, Race, Entry
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
	scores = calculate_scores(entries)
	print scores
	return render(request, 'dd_app/detail.html', 
		{'race': race, 'scores': scores})	


