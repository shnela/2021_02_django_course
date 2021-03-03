from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from customers.serializers import DetailCustomerSerializer, ListCustomerSerializer


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = ListCustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DetailCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'GET':
        serializer = DetailCustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DetailCustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=204)
