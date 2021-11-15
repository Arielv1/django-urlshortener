from django.db import models
from django.utils import timezone

# Create your models here.


class ShortLongUrl(models.Model):
    short = models.CharField(max_length=200, unique=True)
    long = models.CharField(max_length=200)
    time_created = models.DateTimeField(default=timezone.now)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.short, self.long, self.time_created, self.times_used}'
