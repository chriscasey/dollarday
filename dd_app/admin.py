from django.contrib import admin

from .models import Horse, Race, Entry


class EntryInline(admin.TabularInline):
	model = Entry
	extra = 0


class RaceAdmin(admin.ModelAdmin):
	list_display = ('race_number', 'date')
	list_filter = ['date']
	inlines = [EntryInline]	



admin.site.register(Race, RaceAdmin)
admin.site.register(Horse)




