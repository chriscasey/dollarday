from .models import BSF, Entry

def calculate_scores(entries):
	entry_dict = dict((entry.entry_num, entry) for entry in entries)

	bsf_rank_scores = calculate_bsf_rank_scores(entry_dict)
	for bsf_rank in bsf_rank_scores:
		entry_dict[bsf_rank[0]].score = bsf_rank[1]*4

	lifetime_earning_scores = calculate_lifetime_earning_rank_scores(entry_dict)
	for earning_score in lifetime_earning_scores:
		entry_dict[earning_score[0]].score += earning_score[1]*4
	
	win_perc_rank_scores = calculate_lifetime_winning_perc_rank_scores(entry_dict)
	for win_perc_score in win_perc_rank_scores:
		entry_dict[win_perc_score[0]].score += win_perc_score[1]*2		

	return sorted(entry_dict.values(), key=lambda entry: entry.score, reverse=True)

#######################################
# Lifetime winning %
#######################################
def calculate_lifetime_winning_perc_rank_scores(entry_dict):
	winning_perc_by_entry = []
	for entry_num, entry in entry_dict.iteritems():
		winning_perc_by_entry.append( (entry.id, entry.lifetime_win_perc) )
	winning_perc_by_entry.sort(key=lambda tup: tup[1], reverse=True)
	return determine_rank_scores(winning_perc_by_entry)


#######################################
# Average earnings per race this year %
#######################################
def calculate_lifetime_earning_rank_scores(entries):
	earnings_by_entry = []
	for entry_num, entry in entries.iteritems():
		earnings_by_entry.append( (entry.id, entry.avg_earnings) )
	earnings_by_entry.sort(key=lambda tup: tup[1], reverse=True)
	return determine_rank_scores(earnings_by_entry)


#######################################
# BSF Scores
#######################################
def calculate_bsf_rank_scores(entry_dict):
	entry_averages = []
	for entry_num, entry in entry_dict.iteritems():
		bsf_average = calculate_bsf_average(entry)
		entry.avg_speed = bsf_average
		entry_averages.append( (entry.id, bsf_average) )
	entry_averages.sort(key=lambda tup: tup[1], reverse=True)
	return determine_rank_scores(entry_averages)
	

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

def determine_rank_scores(items):
	result = []
	prev = -1
	curr_score = len(items)
	consecutive_dups = 0

	for item in items:
		if item[1] == prev:
			result.append( (item[0], curr_score) )
			consecutive_dups += 1
		else:
			if not prev == -1: ### skip this the first time
				curr_score -= consecutive_dups+1
			result.append( (item[0], curr_score) )
			consecutive_dups = 0
		prev = item[1]	

	return result			




