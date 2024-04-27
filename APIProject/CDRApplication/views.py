from rest_framework import viewsets
from .models import CallDetailRecord
from .serializers import CallDetailRecordSerializer

class CallDetailRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CallDetailRecord.objects.all()
    serializer_class = CallDetailRecordSerializer

from .permissions import IsAuthenticatedOrReadOnly

class CallDetailRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CallDetailRecord.objects.all()
    serializer_class = CallDetailRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

