from django.urls import path

from . import api

urlpatterns = [
    path('customers/', api.CustomerList.as_view()),
    path('customers/<int:pk>/', api.CustomerDetail.as_view()),
]
