from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from places.models import Area, Attraction, Hospital
from places.serializers import AreaSerializer, AttractionSerializer, HospitalSerializer

from server.requests import JSONResponse, haversine


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AttractionList(generics.ListAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionDetail(generics.RetrieveAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class HospitalList(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalDetail(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


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
def hospital_nearest(request, lat, lon):
    """
    Retrieve nearest hospital.
    """

    if request.method == 'GET':

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return JSONResponse(status=400)

        hospitals = Hospital.objects.filter(has_location=True)
        ordered = sorted(hospitals, key=lambda h: haversine(lat, lon, h.latitude, h.longitude))

        if len(ordered) > 0:
            serializer = HospitalSerializer(ordered[0])
            return JSONResponse(serializer.data)

        return HttpResponse(status=404)

    return HttpResponse(status=403)


