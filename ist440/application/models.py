from django.db import models


class MapMarker(models.Model):
    name = models.CharField()
    x_coordinate = models.DecimalField()
    y_coordinate = models.DecimalField()


class InsuranceCard(models.Model):
    company = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField()
    number = models.CharField()
