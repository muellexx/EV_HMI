from django.db import models
from users.models import Company


class ConnectorType(models.Model):
    name = models.CharField(max_length=255)


class ChargingStation(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(default=47.423375435000004)
    lng = models.FloatField(default=7.480080040614551)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    num_points = models.PositiveSmallIntegerField(default=1)
    connector_types = models.ManyToManyField(ConnectorType)


class ChargingPoint(models.Model):
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)


class Connector(models.Model):
    charging_point = models.ForeignKey(ChargingPoint, on_delete=models.CASCADE)
    connector_type = models.ForeignKey(ConnectorType, on_delete=models.PROTECT)
