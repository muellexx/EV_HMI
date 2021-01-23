from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from users.models import Company


class ConnectorType(models.Model):
    name = models.CharField(max_length=255)
    dc_charging = models.BooleanField(default=False, verbose_name='DC Charging')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('connectortype-detail', kwargs={'pk': self.pk})


class ChargingStation(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(default=47.423375435000004, validators=[MaxValueValidator(90), MinValueValidator(-90)])
    lng = models.FloatField(default=7.480080040614551, validators=[MaxValueValidator(180), MinValueValidator(-180)])
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chargingstation-detail', kwargs={'pk': self.pk})

    def get_connectortypes(self):
        return ConnectorType.objects.filter(connector__in=Connector.objects.filter(charging_point__in=ChargingPoint.objects.filter(station=self))).distinct()


    def chargingpoint_count(self):
        return self.chargingpoint_set.count()


class ChargingPoint(models.Model):
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    point_id = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        ordering = ["station", "point_id"]

    def __str__(self):
        return self.station.name + ' - Point ' + str(self.point_id)


class Connector(models.Model):
    charging_point = models.ForeignKey(ChargingPoint, on_delete=models.CASCADE)
    connector_type = models.ForeignKey(ConnectorType, on_delete=models.PROTECT)
    connector_id = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        ordering = ["charging_point", "connector_id"]

    def __str__(self):
        return str(self.charging_point) + ' - Connector ' + str(self.connector_id) + ' (' + self.connector_type.name + ')'
