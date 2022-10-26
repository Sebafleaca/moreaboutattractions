from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
class Favorite(models.Model):
    attraction = models.CharField(max_length=100)
    rating = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.attraction