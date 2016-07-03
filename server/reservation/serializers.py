from rest_framework import serializers
from models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'name', 'num_people', 'date_time', 'res_name', 'res_phone', 'cus_phone', 'status')
