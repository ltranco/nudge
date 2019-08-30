from django.db import models


class Topic(models.Model):
    name = models.TextField(blank=False)
    url = models.URLField()

