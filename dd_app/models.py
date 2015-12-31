from django.db import models
import django_tables2 as tables

class Horse(models.Model):
	name = models.CharField(max_length=50, null=False)

	def __str__(self):
		return self.name

class Raceday(models.Model):
	date = models.DateField(null=False)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return str(self.date)		

class Race(models.Model):
	day = models.ForeignKey(Raceday, null=False)
	race_number = models.IntegerField(default=0)

	def __str__(self):
		return 'race '+ str(self.race_number)+ ' - '+str(self.day) 		

class Entry(models.Model):	
	race = models.ForeignKey(Race, null=False)
	entry_num = models.IntegerField(default=0, verbose_name="Entry")
	finish_pos = models.IntegerField(default=0, verbose_name="Finish Position")
	horse = models.ForeignKey(Horse, null=False, verbose_name="Horse")
	score = models.IntegerField(default=0, verbose_name="Score")
	score_perc = models.FloatField(default=0, verbose_name="Score %")
	score_dfm = models.FloatField(default=0, verbose_name="DFM")
	score_stddev = models.FloatField(default=0, verbose_name="SD")
	highest_bsf = models.IntegerField(default=0, verbose_name="Highest BSF")
	avg_earnings = models.FloatField(default=0, verbose_name="Avg $")
	avg_speed = models.FloatField(default=-1, verbose_name="Avg Speed")
	lifetime_win_perc = models.FloatField(default=0, verbose_name="Lifetime Win %")
	lifetime_starts = models.IntegerField(default=0, verbose_name="Lifetime Starts")
	lifetime_firsts = models.IntegerField(default=0, verbose_name="Lifetime Firsts")
	lifetime_seconds = models.IntegerField(default=0, verbose_name="Lifetime Seconds")
	lifetime_thirds = models.IntegerField(default=0, verbose_name="Lifetime Thirds")
	lifetime_earnings = models.FloatField(default=0, verbose_name="Lifetime Earnings")

	class Meta:
		ordering = ['entry_num']

	def __str__(self):
		return str(str(self.entry_num)+' - '+self.horse.name)


class BSF(models.Model):
	entry = models.ForeignKey(Entry, null=False)
	value = models.FloatField(default=-1)	


class EntryTable(tables.Table):
	class Meta:
		model = Entry
		fields = ("entry_num", "horse", "score", "score_stddev", "score_dfm", "avg_earnings", "avg_speed", "lifetime_win_perc")	
		sequence = ("entry_num", "horse", "score", "score_stddev", "score_dfm", "avg_earnings", "avg_speed", "lifetime_win_perc")	
		attrs = {'class': 'table table-striped table-condensed'}

class WinTable(tables.Table):
	class Meta:
		model = Entry
		fields = ("entry_num", "lifetime_win_perc", "lifetime_starts", "lifetime_firsts", "lifetime_seconds", "lifetime_thirds")	
		sequence = ("entry_num", "lifetime_win_perc", "lifetime_starts", "lifetime_firsts", "lifetime_seconds", "lifetime_thirds")		
		attrs = {'class': 'table table-striped table-condensed'}

class EarningsTable(tables.Table):
	class Meta:
		model = Entry
		fields = ("entry_num", "avg_earnings", "lifetime_earnings", "lifetime_starts")	
		sequence = ("entry_num", "avg_earnings", "lifetime_earnings", "lifetime_starts")		
		attrs = {'class': 'table table-striped table-condensed'}		






