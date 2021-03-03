from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from customers.models import Customer

fake_customer = {'username': 'Olo'}


@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    fake_customers = [fake_customer for _ in range(10)]
    return Response({
        'customers': fake_customers
    })


@api_view(['GET'])
def customer_details(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return Response({
        'customer': customer
    })
