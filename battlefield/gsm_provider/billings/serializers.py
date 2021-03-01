from rest_framework import serializers
from billings.models import Call, ShortMessageService


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['id', 'call_date', 'duration', 'customer']


class ShortMessageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortMessageService
        fields = ['id', 'content', 'send_date', 'customer']
