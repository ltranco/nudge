from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    QUEUED = 'QUE'
    COMPLETED = 'COM'
    CANCELLED = 'CAN'
    ACTIVE = 'ACT'

    STATUSES = (
        (QUEUED, 'Queued'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    )

    owner = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=9999)
    url = models.CharField(blank=True, null=True, max_length=9999)
    status = models.CharField(max_length=3, choices=STATUSES, default=QUEUED)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.status, self.owner)
