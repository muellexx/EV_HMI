from django.contrib import admin
from .models import ConnectorType, ChargingStation, ChargingPoint, Connector


admin.site.register(ConnectorType)
admin.site.register(ChargingStation)
admin.site.register(ChargingPoint)
admin.site.register(Connector)
