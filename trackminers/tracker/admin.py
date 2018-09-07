from django.contrib import admin
from .models import TrackRecord

@admin.register(TrackRecord)
class TrackRecordAdmin(admin.ModelAdmin):
    pass
