from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    distance = models.FloatField(default=0.0)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        