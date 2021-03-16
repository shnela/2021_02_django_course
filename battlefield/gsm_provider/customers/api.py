from django.db.models import Count
from rest_framework import generics

from customers.serializers import ListCustomerSerializer, DetailCustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCustomerSerializer
        elif self.request.method == 'POST':
            return DetailCustomerSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(calls_made_num=Count('calls_made'),
                           calls_received_num=Count('calls_received'),
                           smses_sent_num=Count('smses_sent'),
                           smses_received_num=Count('smses_received'),
                           ).all()


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailCustomerSerializer
