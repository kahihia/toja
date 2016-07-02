from rest_framework import serializers
from places.models import Area, Attraction, Hospital


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'description')


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'address', 'address_jp', 'description', 'images', 'area',
                  'has_location', 'latitude', 'longitude')


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'address', 'tel', 'hours', 'after_hours', 'url',
                  'image', 'has_location', 'latitude', 'longitude')
