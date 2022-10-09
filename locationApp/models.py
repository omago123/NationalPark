from django.db import models

class test(models.Model):
    park_name = models.CharField(max_length=100)
    park_latitude = models.FloatField()
    park_longitude = models.FloatField()
    class Meta:
        db_table = 'park'
        managed = False


class state(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        db_table = 'state'