from django.db import models
from django.conf import settings
from martor.models import MartorField

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = MartorField()