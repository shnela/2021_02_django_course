from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from customers.models import Customer
import re


class PhoneField(serializers.Field):
    def to_representation(self, value):
        return f'+48 {value}'

    def to_internal_value(self, data):
        match_pattern = re.match(r'^\d{3}(-\d{3}){2}$', data)
        if not match_pattern:
            raise ValidationError('Expecting data of format: "XXX-XXX-XXX"')
        return data


class CourseValidator:
    def __init__(self):
        pass

    def __call__(self, value):
        pass


class CustomerSerializer(serializers.ModelSerializer):
    msisdn = PhoneField(required=False)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'type', 'msisdn']
        validators = [
            CourseValidator()
        ]
