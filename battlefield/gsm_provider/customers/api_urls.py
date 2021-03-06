from django.urls import path

from . import api
from .models import Customer

urlpatterns = [
    path('business/', api.CustomerList.as_view(
        queryset=Customer.business.all()
    )),
    path('business/<int:pk>/', api.CustomerDetail.as_view(
        queryset=Customer.business.all()
    )),
]
