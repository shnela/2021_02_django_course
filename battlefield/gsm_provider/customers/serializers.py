import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from billings.models import Call
from customers.models import Customer


class PhoneField(serializers.Field):
    def to_representation(self, value):
        return f'+48 {value}'

    def to_internal_value(self, data):
        match_pattern = re.match(r'^\+48 (\d{3}(-\d{3}){2})$', data)
        if not match_pattern:
            raise ValidationError('Expecting data of format: "+48 XXX-XXX-XXX"')
        return match_pattern.group(1)


class DetailCustomerSerializer(serializers.ModelSerializer):
    msisdn = PhoneField()

    class Meta:
        model = Customer
        fields = '__all__'


class SimpleCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['call_date', 'duration']


class ListCustomerSerializer(serializers.ModelSerializer):
    calls_made_num = serializers.IntegerField(read_only=True)
    calls_received_num = serializers.IntegerField(read_only=True)
    smses_sent_num = serializers.IntegerField(read_only=True)
    smses_received_num = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'calls_made_num', 'calls_received_num',
                  'smses_sent_num', 'smses_received_num']
