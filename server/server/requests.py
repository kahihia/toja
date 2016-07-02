from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from math import radians, cos, sin, asin, sqrt


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees).

    https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
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
