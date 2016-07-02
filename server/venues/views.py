from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from venues.models import Venue, Category
from venues.serializers import VenueSerializer, CategorySerializer

from server.requests import JSONResponse, haversine


class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class VenueDetail(generics.RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@csrf_exempt
def venue_nearby(request, lat, lon):

    venues = Venue.objects.all()
    venues = [v for v in venues if haversine(float(lon), float(lat), float(v.longitude), float(v.latitude)) < 0.5]

    serializer = VenueSerializer(venues, many=True)
    response = JSONResponse(serializer.data)
    return response


@csrf_exempt
def category_venues(request, pk):
    """
    Retrieve venues catering to requested category.
    """
    try:
        print('finding ' + pk)
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    venues = Venue.objects.filter(categories__pk=pk)

    if request.method == 'GET':
        serializer = VenueSerializer(venues, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)
