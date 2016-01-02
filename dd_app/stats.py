from django.shortcuts import get_object_or_404, get_list_or_404, render
from django_tables2 import RequestConfig
from django.http import JsonResponse
import math
from analyzer import *
import numpy as np
from .models import Raceday, Race, Entry, RaceResult

def results_all(request):
	race_list = get_list_or_404(Race)
	result_list = []
	for race in race_list:
		result_list.append(compute_race_stats(race))

	score_win_count = 0
	score_exa_count = 0
	score_tri_count = 0
	score_sf_count = 0
	avg_earning_win_count = 0
	avg_earning_exa_count = 0
	avg_earning_tri_count = 0
	avg_earning_sf_count = 0
	win_perc_win_count = 0
	win_perc_exa_count = 0
	win_perc_tri_count = 0
	win_perc_sf_count = 0
	avg_speed_win_count = 0
	avg_speed_exa_count = 0
	avg_speed_tri_count = 0
	avg_speed_sf_count = 0

	for result in result_list:
		if result.score_win_predicted:
			score_win_count +=1
		if result.score_exa_predicted:
			score_exa_count +=1
		if result.score_tri_predicted:
			score_tri_count +=1
		if result.score_sf_predicted:
			score_sf_count +=1
		
		if result.avg_earning_win_predicted:
			avg_earning_win_count += 1
		if result.avg_earning_exa_predicted:
			avg_earning_exa_count += 1
		if result.avg_earning_tri_predicted:
			avg_earning_tri_count += 1
		if result.avg_earning_sf_predicted:
			avg_earning_sf_count += 1	

		if result.win_perc_win_predicted:
			win_perc_win_count += 1
		if result.win_perc_exa_predicted:
			win_perc_exa_count += 1
		if result.win_perc_tri_predicted:
			win_perc_tri_count += 1
		if result.win_perc_sf_predicted:
			win_perc_sf_count += 1	

		if result.avg_speed_win_predicted:
			avg_speed_win_count += 1
		if result.avg_speed_exa_predicted:
			avg_speed_exa_count += 1
		if result.avg_speed_tri_predicted:
			avg_speed_tri_count += 1
		if result.avg_speed_sf_predicted:
			avg_speed_sf_count += 1							

	result_count = len(result_list)
	score_win_perc = round(float(score_win_count)/result_count*100),2)
	score_exa_perc = round(float(score_exa_count)/result_count*100),2)
	score_tri_perc = round(float(score_tri_count)/result_count*100),2)
	score_sf_perc = round(float(score_sf_count)/result_count*100),2)
	avg_earnings_win_perc = round(float(avg_earning_win_count)/result_count*100),2)
	avg_earnings_exa_perc = round(float(avg_earning_exa_count)/result_count*100),2)
	avg_earnings_tri_perc = round(float(avg_earning_tri_count)/result_count*100),2)
	avg_earnings_sf_perc = round(float(avg_earning_sf_count)/result_count*100),2)

	win_perc_win_perc = round(float(win_perc_win_count)/result_count*100),2)
	win_perc_exa_perc = round(float(win_perc_exa_count)/result_count*100),2)
	win_perc_tri_perc = round(float(win_perc_tri_count)/result_count*100),2)
	win_perc_sf_perc = round(float(win_perc_sf_count)/result_count*100),2)

	avg_speed_win_perc = round(float(avg_speed_win_count)/result_count*100),2)
	avg_speed_exa_perc = round(float(avg_speed_exa_count)/result_count*100),2)
	avg_speed_tri_perc = round(float(avg_speed_tri_count)/result_count*100),2)
	avg_speed_sf_perc = round(float(avg_speed_sf_count)/result_count*100),2)

	context = {'score_win_perc': score_win_perc,
	'score_exa_perc': score_exa_perc, 
	'score_tri_perc':score_tri_perc, 
	'score_sf_perc':score_sf_perc,
	'avg_earnings_win_perc':avg_earnings_win_perc,
	'avg_earnings_exa_perc':avg_earnings_exa_perc,
	'avg_earnings_tri_perc':avg_earnings_tri_perc,
	'avg_earnings_sf_perc':avg_earnings_sf_perc,
	'win_perc_win_perc': win_perc_win_perc,
	'win_perc_exa_perc':win_perc_exa_perc,
	'win_perc_tri_perc':win_perc_tri_perc,
	'win_perc_sf_perc':win_perc_sf_perc,
	'avg_speed_win_perc':avg_speed_win_perc,
	'avg_speed_exa_perc':avg_speed_exa_perc,
	'avg_speed_tri_perc':avg_speed_tri_perc,
	'avg_speed_sf_perc':avg_speed_sf_perc}
	return render(request, 'dd_app/stats.html', context)

def results_by_year(request, year):
	context = {'hello': 'hello'}
	return render(request, 'dd_app/stats.html', context)


def compute_race_stats(race):
	try:
		race_result = RaceResult.objects.get(race__id=race.id)
	except RaceResult.DoesNotExist:
		race_result = RaceResult.create_result(race)

	entries = Entry.objects.all().filter(race__id=race.id)
	entries = calculate_scores(entries)
	actual_results = build_single_race_result_list(entries)
	if actual_results:
		race_result = compare_score_prediction_with_result(entries, actual_results, race_result)		
		race_result = compare_avg_earning_prediction_with_result(entries, actual_results, race_result)
		race_result = compare_win_perc_prediction_with_result(entries, actual_results, race_result)
		race_result = compare_avg_speed_prediction_with_result(entries, actual_results, race_result)
		race_result.save()
	return race_result

def compare_score_prediction_with_result(entries, actual_results, race_result):
	sorted_by_score = sorted(entries, key=lambda entry: entry.score, reverse=True)
	sorted_entries = [entry.entry_num for entry in sorted_by_score]
	if compare(sorted_entries, actual_results, 1):
		race_result.score_win_predicted = True
	if compare(sorted_entries, actual_results, 2):
		race_result.score_exa_predicted = True
	if compare(sorted_entries, actual_results, 3):
		race_result.score_tri_predicted = True
	if compare(sorted_entries, actual_results, 4):
		race_result.score_sf_predicted = True
	return race_result

def compare_avg_earning_prediction_with_result(entries, actual_results, race_result):
	sorted_by_avg_earning = sorted(entries, key=lambda entry: entry.avg_earnings, reverse=True)
	sorted_entries = [entry.entry_num for entry in sorted_by_avg_earning]
	if compare(sorted_entries, actual_results, 1):
		race_result.score_win_predicted = True
	if compare(sorted_entries, actual_results, 2):
		race_result.avg_earning_exa_predicted = True
	if compare(sorted_entries, actual_results, 3):
		race_result.avg_earning_tri_predicted = True
	if compare(sorted_entries, actual_results, 4):
		race_result.avg_earning_sf_predicted = True
	return race_result	

def compare_win_perc_prediction_with_result(entries, actual_results, race_result):
	sorted_by_win_perc = sorted(entries, key=lambda entry: entry.lifetime_win_perc, reverse=True)
	sorted_entries = [entry.entry_num for entry in sorted_by_win_perc]
	if compare(sorted_entries, actual_results, 1):
		race_result.win_perc_win_predicted = True
	if compare(sorted_entries, actual_results, 2):
		race_result.win_perc_exa_predicted = True
	if compare(sorted_entries, actual_results, 3):
		race_result.win_perc_tri_predicted = True
	if compare(sorted_entries, actual_results, 4):
		race_result.win_perc_sf_predicted = True
	return race_result	

def compare_avg_speed_prediction_with_result(entries, actual_results, race_result):
	sorted_by_avg_speed = sorted(entries, key=lambda entry: entry.avg_speed, reverse=True)
	sorted_entries = [entry.entry_num for entry in sorted_by_avg_speed]
	if compare(sorted_entries, actual_results, 1):
		race_result.avg_speed_win_predicted = True
	if compare(sorted_entries, actual_results, 2):
		race_result.avg_speed_exa_predicted = True
	if compare(sorted_entries, actual_results, 3):
		race_result.avg_speed_tri_predicted = True
	if compare(sorted_entries, actual_results, 4):
		race_result.avg_speed_sf_predicted = True
	return race_result			

def compare(predicted, actual, index):
	predicted_slice = sorted(predicted[:index])
	actual_slice = sorted(actual[:index])
	return actual_slice == predicted_slice

def build_single_race_result_list(entries):
	result = []
	for entry in entries:
		if entry.finish_pos == 1:
			result.insert(1, entry.entry_num)
		elif entry.finish_pos == 2:
			result.insert(2, entry.entry_num)
		elif entry.finish_pos == 3:
			result.insert(3, entry.entry_num)
		elif entry.finish_pos == 4:
			result.insert(4, entry.entry_num)
	return result		

