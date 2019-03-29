import csv

from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from django.conf import settings
from django.core.paginator import Paginator


def create_paginator():
	database = []
	with open(settings.BUS_STATION_CSV, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			database.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
	return Paginator(database, 10)



def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
	paginator = create_paginator()
	current_page = int(request.GET.get('page'))
	next_page_url = f'bus_stations?page={current_page + 1}'

	if current_page < 2:
		prev_page_url = None
	else:
		prev_page_url = f'bus_stations?page={current_page - 1}'

	return render_to_response('index.html', context = {
		'bus_stations': paginator.page(current_page),
		'current_page': current_page,
		'prev_page_url': prev_page_url,
		'next_page_url': next_page_url
	})

