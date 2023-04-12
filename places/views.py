from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lat, place.lon]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": "static/places/moscow_legends.json"
            }
        })
    places_geojson = {"type": "FeatureCollection",
               "features": features}
    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)

