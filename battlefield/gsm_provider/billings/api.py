from rest_framework import generics

from billings.models import Call, ShortMessageService
from billings.serializers import CallSerializer, ShortMessageServiceSerializer


class CallList(generics.ListCreateAPIView):
    queryset = Call.objects.select_related('caller', 'callee').all()
    serializer_class = CallSerializer


class CallDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class ShortMessageServiceList(generics.ListCreateAPIView):
    queryset = ShortMessageService.objects.select_related('sending_party', 'sent_party').all()
    serializer_class = ShortMessageServiceSerializer


class ShortMessageServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortMessageService.objects.all()
    serializer_class = ShortMessageServiceSerializer
