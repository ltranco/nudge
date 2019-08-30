from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    owner = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=9999)
    url = models.CharField(blank=True, null=True, max_length=9999)
    is_completed = models.BooleanField(default=False)
