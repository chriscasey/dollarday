from django.db import models

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
	entry_num = models.IntegerField(default=0)
	horse = models.ForeignKey(Horse, null=False)
	score = models.IntegerField(default=0)
	highest_bsf = models.IntegerField(default=0)
	avg_earnings = models.FloatField(default=0)
	avg_speed = models.FloatField(default=-1)
	lifetime_win_perc = models.FloatField(default=0)

	class Meta:
		ordering = ['entry_num']

	def __str__(self):
		return str(str(self.entry_num)+' - '+self.horse.name)


class BSF(models.Model):
	entry = models.ForeignKey(Entry, null=False)
	value = models.FloatField(default=-1)		


