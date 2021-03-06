from django.db import models

# Create your models here.

class GeoArea(models.Model):
    geo_json = models.TextField(null=True)
    area = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    level = models.IntegerField(default=0)
    prefix = models.CharField(max_length=10)
    is_hot = models.IntegerField(default=0)
    cp_latitude = models.FloatField(default=0)
    cp_longitude = models.FloatField(default=0)

    def __str__(self):
        return "%s-%s" % (self.name, self.code)

