from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    owner = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    url = models.URLField()
    is_completed = models.BooleanField(default=False)
