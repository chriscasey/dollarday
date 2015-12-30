from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import BSF, Horse, Entry, Race, Raceday	

class BSFInline(admin.TabularInline):
	model = BSF
	extra = 0

class EntryInline(admin.TabularInline):
	model = Entry
	fields = ['race', 'entry_num', 'horse', 'finish_pos']	
	extra = 0

class EntryAdmin(admin.ModelAdmin):
	list_filter = ['entry_num']
	inlines = [BSFInline]

class RaceInline(admin.TabularInline):
	model = Race
	extra = 0

class RaceAdmin(admin.ModelAdmin):
	list_filter = ['day__date', 'race_number']
	inlines = [EntryInline]

class RacedayAdmin(admin.ModelAdmin):
	list_filter = ['date']
	inlines = [RaceInline]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Raceday, RacedayAdmin)
admin.site.register(Horse)




