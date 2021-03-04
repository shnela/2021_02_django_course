from rest_framework import generics, permissions

from customers.models import Customer
from customers.serializers import ListCustomerSerializer, DetailCustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCustomerSerializer
        elif self.request.method == 'POST':
            return DetailCustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()
    serializer_class = DetailCustomerSerializer
