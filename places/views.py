from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from places.models import Place


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    detailsUrl = {"title": place.title,
                  'imgs': [image.image.url for image in place.images.all()],
                  'description_short': place.short_description,
                  'description_long': place.long_description,
                  'coordinates': {'lat': place.lat, 'lng': place.lon}}
    response = JsonResponse(detailsUrl, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return response


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
