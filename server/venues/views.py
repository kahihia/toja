from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from venues.models import Venue
from venues.serializers import VenueSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def venue_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Venue.objects.all()
        serializer = VenueSerializer(snippets, many=True)
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
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Venue.objects.get(pk=pk)
    except Venue.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VenueSerializer(snippet)
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
