from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('event/', views.event_from_get, name='event_from_get'),
    path('event/<yyyy:year>/', views.event_from_kwargs, name='event_from_kwargs'),
]
