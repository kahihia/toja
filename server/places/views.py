from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from places.models import Area, Attraction, Hospital
from places.serializers import AreaSerializer, AttractionSerializer, HospitalSerializer

from server.requests import JSONResponse


@csrf_exempt
def area_list(request):
    """
    List all venues.
    """
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def area_detail(request, pk):
    """
    Retrieve individual venue.
    """
    try:
        area = Area.objects.get(pk=pk)
    except Area.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AreaSerializer(area)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def area_attractions(request, pk):
    """
    Get list of attractions at given area.
    """
    try:
        area = Area.objects.get(pk=pk)
    except Area.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        attractions = Attraction.objects.filter(area__pk=pk)
        serializer = AttractionSerializer(attractions, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def attraction_list(request):
    """
    List all venues.
    """
    if request.method == 'GET':
        snippets = Attraction.objects.all()
        serializer = AttractionSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def attraction_detail(request, pk):
    """
    Retrieve individual venue.
    """
    try:
        venue = Attraction.objects.get(pk=pk)
    except Attraction.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AttractionSerializer(venue)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def hospital_list(request):
    """
    List all hospitals.
    """
    if request.method == 'GET':
        snippets = Hospital.objects.all()
        serializer = HospitalSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


@csrf_exempt
def hospital_detail(request, pk):
    """
    Retrieve individual hospital.
    """
    try:
        venue = Hospital.objects.get(pk=pk)
    except Hospital.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HospitalSerializer(venue)
        return JSONResponse(serializer.data)

    return JSONResponse(status=403)


