from rest_framework import generics

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('calls_made').all()


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
