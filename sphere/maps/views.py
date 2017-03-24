from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from maps.models import Country
from maps.forms import CountryForm


def country_list(request):
    countries = Country.objects.all()[:20]
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CountryForm()
    else:
        form = CountryForm()
        
    return render(
        request, 'maps/country_list.html',
        {'countries': countries, 'form': form}
    )
    #return JsonResponse({
    #    'countries': [
    #        {'name': c.name, 'id': c.id} for c in countries
    #    ]
    #})


def country_detail(request, country_id):
    try:
        country = Country.objects.get(id=country_id) 
    except Country.DoesNotExist:
        raise Http404('No such country')
    result = '<h1>{0}</h1>'.format(country.name)
    cities = country.cities.all()
    for city in cities:
        result += '<h2>{0}</h2>'.format(city.name)
    return HttpResponse(result)
