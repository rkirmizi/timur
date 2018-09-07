from rest_framework import serializers
from .models import TrackRecord

class TrackRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRecord
        fields = '__all__'
