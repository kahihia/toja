from rest_framework import serializers
from places.models import Area, Attraction


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'description')


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'address', 'address_jp', 'description', 'images', 'area',
                  'has_location', 'latitude', 'longitude')
