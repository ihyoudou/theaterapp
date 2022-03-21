from django.db import models
from core.models import Movies
from django.conf import settings
# Create your models here.

class Orders(models.Model):
    ordered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False
    )
    item = models.ForeignKey(Movies, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)