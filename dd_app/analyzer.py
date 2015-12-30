from .models import BSF, Entry
import numpy as np
from operator import itemgetter

BSF_RANK_WEIGHT=4
LIFETIME_EARNING_RANK_WEIGHT=4
WIN_PERC_RANK_WEIGHT=2
SCORE_RANGE=10

def calculate_scores(entries):
	entry_dict = dict((entry.entry_num, entry) for entry in entries)

	bsf_rank_scores = calculate_bsf_rank_scores(entry_dict)
	for bsf_rank in bsf_rank_scores:
		entry_dict[bsf_rank[0]].score = bsf_rank[1]

	lifetime_earning_scores = calculate_lifetime_earning_rank_scores(entry_dict)
	for lifetime_earning_score in lifetime_earning_scores:
		entry_dict[lifetime_earning_score[0]].score += lifetime_earning_score[1]
	
	win_perc_rank_scores = calculate_lifetime_winning_perc_rank_scores(entry_dict)
	for win_perc_score in win_perc_rank_scores:
		entry_dict[win_perc_score[0]].score += win_perc_score[1]		

	return sorted(entry_dict.values(), key=lambda entry: entry.score, reverse=True)

#######################################
# Lifetime winning %
#######################################
def calculate_lifetime_winning_perc_rank_scores(entry_dict):
	winning_perc_by_entry = []
	for entry_num, entry in entry_dict.iteritems():
		if entry.lifetime_win_perc == 0 and entry.lifetime_starts > 0:
			lifetime_win_perc = round((entry.lifetime_firsts + entry.lifetime_seconds + entry.lifetime_thirds) / float(entry.lifetime_starts),2)
			entry.lifetime_win_perc = lifetime_win_perc
			entry.save()
		winning_perc_by_entry.append( (entry.entry_num, entry.lifetime_win_perc) )
	return scale_scores(winning_perc_by_entry, WIN_PERC_RANK_WEIGHT)


#######################################
# Average earnings per race this year %
#######################################
def calculate_lifetime_earning_rank_scores(entries):
	earnings_by_entry = []
	for entry_num, entry in entries.iteritems():
		earnings_by_entry.append( (entry.entry_num, entry.avg_earnings) )
	return scale_scores(earnings_by_entry, LIFETIME_EARNING_RANK_WEIGHT)


#######################################
# BSF Scores
#######################################
def calculate_bsf_rank_scores(entry_dict):
	entry_averages = []
	for entry_num, entry in entry_dict.iteritems():
		bsf_average = calculate_bsf_average(entry)
		entry.avg_speed = bsf_average
		entry_averages.append( (entry.entry_num, entry.avg_speed) )
	return scale_scores(entry_averages, BSF_RANK_WEIGHT)
	

def calculate_bsf_average(entry):
	bsf_list = BSF.objects.filter(entry_id=entry.id)
	if bsf_list:
		sum = 0
		for bsf_entry in bsf_list:
			sum += bsf_entry.value
		if sum > 0:
			return sum/len(bsf_list)
		else:
			return 0	
	return 0		

def scale_scores(items, weight):
	max_score = max(items, key=itemgetter(1))[1]
	min_score = min(items, key=itemgetter(1))[1]
	old_range = max_score - min_score
	result = []
	for item in items:
		scaled_score = ((((item[1] - min_score) * 10) / old_range) + 0) * weight
		result.append( (item[0], scaled_score) )
	return result

def compute_spread_data(items):
	scores = sorted([item.score for item in items ])
	return round(np.mean(scores),2), round(np.std(scores),2), round(np.var(scores),2)

def compute_mean_deviation(mean, items):
	distances_from_mean = []
	for item in items:
		dfm = 0
		if item.score > mean:
			dfm = item.score-mean
		else:
			dfm = mean-item.score	
		distances_from_mean.append(dfm)
	return round(np.mean(distances_from_mean), 2)

def compute_distance_scores(entries, mean, stddev, mean_dev):
	for entry in entries:
		entry.score_stddev = round((entry.score/stddev),2)
		if entry.score < mean:
			entry.score_stddev = entry.score_stddev*-1
		entry.score_dfm = round((entry.score/mean_dev),2)
		if entry.score < mean:
			entry.score_dfm = entry.score_dfm*-1
	return entries	

def compute_min_max():
	min = 0
	max = (SCORE_RANGE*BSF_RANK_WEIGHT)+(SCORE_RANGE*LIFETIME_EARNING_RANK_WEIGHT)+(SCORE_RANGE*WIN_PERC_RANK_WEIGHT)
	return min, max	

def compute_score_perc(entries, max_score):
	for entry in entries:
		entry.score_perc = round((float(entry.score)/max_score)*100, 2)
	return entries	




