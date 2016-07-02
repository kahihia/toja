from rest_framework import serializers
from models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'name', 'num_people', 'date', 'time', 'res_num', 'status', 'language_opt')
