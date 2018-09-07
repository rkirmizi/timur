from rest_framework.viewsets import ModelViewSet
from .models import TrackRecord
from .serializers import TrackRecordSerializer


class TrackRecordViewSet(ModelViewSet):
    queryset = TrackRecord.objects.all()
    serializer_class = TrackRecordSerializer
