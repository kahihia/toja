from rest_framework import serializers
from models import Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('name', 'gurunavi_id', 'gurunavi_url', 'address', 'latitude', 'longditude', 'images')