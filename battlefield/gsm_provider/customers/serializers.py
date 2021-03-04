from rest_framework import serializers

from billings.models import Call
from customers.models import Customer


class DetailCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SimpleCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['call_date', 'duration']


class ListCustomerSerializer(serializers.ModelSerializer):
    calls_made_num = serializers.IntegerField(source='calls_made.count', read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'calls_made_num']
