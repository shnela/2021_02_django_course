from django.db.models import Count
from rest_framework import generics

from customers.serializers import ListCustomerSerializer, DetailCustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCustomerSerializer
        elif self.request.method == 'POST':
            return DetailCustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailCustomerSerializer
