from rest_framework import serializers

from billings.models import Call
from customers.models import Customer


class SimpleCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['call_date', 'duration']


class CustomerSerializer(serializers.ModelSerializer):
    calls_made = SimpleCallSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'type', 'calls_made']
