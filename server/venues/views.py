from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from venues.models import Venue, Category
from venues.serializers import VenueSerializer, CategorySerializer

from server.requests import JSONResponse

@csrf_exempt
def venue_list(request):
    """
    List all venues.
    """
    if request.method == 'GET':
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = VenueSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data, status=201)
    #     return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def venue_detail(request, pk):
    """
    Retrieve individual venue.
    """
    try:
        venue = Venue.objects.get(pk=pk)
    except Venue.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VenueSerializer(venue)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = VenueSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data)
    #     return JSONResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)


@csrf_exempt
def venue_nearby(request, lat, lon):

    # https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points

    from math import radians, cos, sin, asin, sqrt

    def haversine(lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        print(lon1, lat1, lon2, lat2)

        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2.0)**2.0 + cos(lat1) * cos(lat2) * sin(dlon/2.0)**2.0
        c = 2.0 * asin(sqrt(a))
        km = 6367.0 * c
        return km

    venues = Venue.objects.all()
    venues = [venue for venue in venues if haversine(float(lon), float(lat), float(venue.longitude), float(venue.latitude)) < 0.5]
    print(len(venues))

    serializer = VenueSerializer(venues, many=True)
    response = JSONResponse(serializer.data)
    return response

@csrf_exempt
def category_list(request):
    """
    List all categories.
    """
    if request.method == 'GET':
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


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
