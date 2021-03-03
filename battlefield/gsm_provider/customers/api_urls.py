from django.urls import path

from . import api

urlpatterns = [
    path('customers/', api.customer_list),
    path('customers/<int:customer_id>/', api.customer_details),
]
