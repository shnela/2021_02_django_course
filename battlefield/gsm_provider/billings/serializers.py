from rest_framework import serializers
from billings.models import Call, ShortMessageService
from customers.models import Customer


class SimpleCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username']


class CallSerializer(serializers.ModelSerializer):
    caller = SimpleCustomerSerializer()
    callee = SimpleCustomerSerializer()

    class Meta:
        model = Call
        fields = ['id', 'call_date', 'duration', 'caller', 'callee']


class ShortMessageServiceSerializer(serializers.ModelSerializer):
    sending_party = SimpleCustomerSerializer()
    sent_party = SimpleCustomerSerializer()

    class Meta:
        model = ShortMessageService
        fields = ['id', 'content', 'send_date', 'sending_party', 'sent_party']
