from django.conf import settings
from django.db import models


class InsuranceCard(models.Model):
    company = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class MapMarker(models.Model):
    name = models.CharField(max_length=255)
    x_coordinate = models.DecimalField(decimal_places=3, max_digits=6)
    y_coordinate = models.DecimalField(decimal_places=3, max_digits=6)
