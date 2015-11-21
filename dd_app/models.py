from django.db import models

class Horse(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Race(models.Model):
	date = models.DateField('date')
	race_number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.race_number) 	

class Entry(models.Model):	
	race = models.ForeignKey(Race)
	entry_num = models.IntegerField(default=0)
	horse = models.ForeignKey(Horse)
	score = models.IntegerField(default=0)
	highest_bsf = models.IntegerField(default=0)
	avg_earnings = models.FloatField(default=0)
	avg_speed = models.FloatField(default=0)
	lifetime_win_perc = models.FloatField(default=0)

	class Meta:
		ordering = ['entry_num']

	def __str__(self):
		return str(str(self.entry_num)+' - '+self.horse.name)


