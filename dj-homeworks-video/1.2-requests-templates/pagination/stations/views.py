from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv_file():
    station_information = []

    with open('pagination/data-398-2018-08-30.csv', encoding='utf-8') as file:
        information = csv.reader(file)
        for row in information:
            if row[1] != 'Name' or row[4] != 'Street' or row[6] != 'District':
                station_information.append({
                    'Name': row[1],
                    'Street': row[4],
                    'District': row[6]
                })

    return station_information

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    stations_information = read_csv_file()
    template_name = 'stations/index.html'
    paginator = Paginator(stations_information, 5)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }

    return render(request, template_name, context)
