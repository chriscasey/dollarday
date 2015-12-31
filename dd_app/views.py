from django.shortcuts import get_object_or_404, get_list_or_404, render
from django_tables2 import RequestConfig
from django.http import JsonResponse
import math

from .models import Raceday, Race, Entry, EntryTable, WinTable, EarningsTable
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
	max_score = compute_max_score()
	results = format_results(entries_with_dist_data)
	table = EntryTable(entries_with_dist_data)
	win_table = WinTable(entries_with_dist_data)
	earnings_table = EarningsTable(entries_with_dist_data)
	RequestConfig(request).configure(table)
	return render(request, 'dd_app/detail.html', {'table': table, 'win_table':win_table, 
		'race': race, 'results': results, 'earnings_table': earnings_table})

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

def scatter_plot_graph(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	entries_with_scores = calculate_scores(entries)
	data = []
	prev_score = 0
	y_val = 1
	for entry in entries_with_scores:
		horse = ' ('+str(entry.entry_num)+') '+entry.horse.name
		if entry.score == prev_score:
			y_val += 1
		else:
			y_val = 1	
		data.append({'horse':horse, 'score':entry.score, 'num':y_val})
		prev_score = entry.score	
	return JsonResponse(data, safe=False)

def box_plot_chart(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	entries_with_scores = calculate_scores(entries)
	data = []
	for entry in entries_with_scores:
		e = {'entry_num': entry.entry_num}
		bsf_items = get_list_or_404(BSF, entry=entry.id)
		bsf_scores = [s.value for s in bsf_items]
		e['bsf_scores'] = bsf_scores 
		data.append(e)
	return JsonResponse(data, safe=False)	

def lifetime_win_bar_chart(request, race_id):
	data = []
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	entries_with_scores = calculate_scores(entries)
	data = []
	for entry in entries_with_scores:
		data.append({'entry': entry.entry_num, 'frequency': entry.lifetime_win_perc})
	return JsonResponse(data, safe=False) 

def lifetime_win_grouped(request, race_id):
	data = []
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	for entry in entries:
		row = {'entry_num': entry.entry_num,
		'lifetime_starts': entry.lifetime_starts,
		'lifetime_firsts': entry.lifetime_firsts,
		'lifetime_seconds': entry.lifetime_seconds,
		'lifetime_thirds': entry.lifetime_thirds}
		data.append(row)
	return JsonResponse(data, safe=False) 

def lifetime_win_bullet_chart(request, race_id):
	data = []
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	for entry in entries:
		third_place_marker = entry.lifetime_thirds
		second_place_marker = entry.lifetime_thirds + entry.lifetime_seconds
		first_place_marker = entry.lifetime_thirds + entry.lifetime_seconds + entry.lifetime_firsts
		row = {"title": entry.entry_num, "subtitle": entry.horse.name,
		"ranges":[first_place_marker, entry.lifetime_starts], 
		"measures":[third_place_marker, second_place_marker, first_place_marker], 
		"markers":[third_place_marker, second_place_marker, first_place_marker]}
		data.append(row)
	return JsonResponse(data, safe=False) 	

def average_earnings_bullet_chart(request, race_id):
	data = []
	race = get_object_or_404(Race, pk=race_id)
	entries = get_list_or_404(Entry, race=race.id)
	max_avg = 1180
	for entry in entries:
		avg_earnings = float(entry.lifetime_earnings)/entry.lifetime_starts
		row = {"title": entry.entry_num, "subtitle": entry.horse.name,
		"ranges":[max_avg], 
		"measures":[avg_earnings], 
		"markers":[avg_earnings]}
		data.append(row)
	return JsonResponse(data, safe=False)	






