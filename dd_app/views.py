from django.shortcuts import get_object_or_404, get_list_or_404, render
from django_tables2 import RequestConfig
from django.http import JsonResponse
import math

from .models import Raceday, Race, Entry, EntryTable
from analyzer import *
def index(request):
	latest_raceday_list = Raceday.objects.order_by('-date')[:5]
	context = {'latest_raceday_list': latest_raceday_list}
	return render(request, 'dd_app/index.html', context)

def races_list(request, raceday_id):
	races_list = get_list_or_404(Race, day=raceday_id)
	raceday = get_object_or_404(Raceday, pk=raceday_id)
	return render(request, 'dd_app/race_list.html', {'raceday':raceday, 'races_list': races_list})


def race_detail(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race_id)
	entries_with_scores = calculate_scores(entries)
	mean, stdev, variance = compute_spread_data(entries_with_scores)
	mean_dev = compute_mean_deviation(mean, entries_with_scores)
	entries_with_dist_data = compute_distance_scores(entries_with_scores, mean, stdev, mean_dev)
	min_score, max_score = compute_min_max(len(entries_with_dist_data))
	table = EntryTable(entries_with_scores)
	RequestConfig(request).configure(table)
	return render(request, 'dd_app/detail.html', {'table': table, 'race': race, 
		'mean': mean, 'stdev':stdev, 'variance':variance, 'mean_dev': mean_dev, 
		'min_score':min_score, 'max_score':max_score})

def score_pie_chart(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	entries_with_scores = calculate_scores(entries)
	sum_of_scores = float(sum(entry.score for entry in entries_with_scores))
	data = []
	for entry in entries_with_scores:
		perc = math.floor(float(entry.score/sum_of_scores)*100)
		horse = ' ('+str(entry.entry_num)+') '+entry.horse.name+' '+str(perc)+'%'
		data.append({'horse': horse, 'score': entry.score})
	return JsonResponse(data, safe=False)	


