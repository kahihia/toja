from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from venues.models import Venue, Category
from venues.serializers import VenueSerializer, CategorySerializer

from server.requests import JSONResponse, haversine

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

    venues = Venue.objects.all()
    venues = [v for v in venues if haversine(float(lon), float(lat), float(v.longitude), float(v.latitude)) < 0.5]

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
