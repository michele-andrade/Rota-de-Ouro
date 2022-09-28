from djongo import models


class Touristplace(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    time = models.TextField()
    payment = models.TextField()
    adress = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    accessibility = models.TextField()