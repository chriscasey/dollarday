from django.shortcuts import get_object_or_404, render

from .models import Race

def index(request):
	latest_race_list = Race.objects.order_by('-date')[:5]
	context = {'latest_race_list': latest_race_list}
	return render(request, 'dd_app/index.html', context)


def race_detail(request, race_id):
	race = get_object_or_404(Race, pk=race_id)
	return render(request, 'dd_app/detail.html', {'race': race})	


