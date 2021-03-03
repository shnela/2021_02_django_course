from django.urls import path

from . import api

urlpatterns = [
    path('calls/', api.CallList.as_view()),
    path('calls/<int:pk>/', api.CallDetail.as_view()),
    path('sms/', api.ShortMessageServiceList.as_view()),
    path('sms/<int:pk>/', api.ShortMessageServiceDetail.as_view()),
]
