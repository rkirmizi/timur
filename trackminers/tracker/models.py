from django.db import models


class TrackRecord(models.Model):
    node_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    sols_s = models.DecimalField(max_digits=5, decimal_places=2)
