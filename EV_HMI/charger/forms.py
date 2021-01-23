from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import ChargingStation, ConnectorType


class ChargingStationForm(forms.ModelForm):
    connectortype = forms.ModelMultipleChoiceField(queryset=ConnectorType.objects.all(), label='Available Connector Types')
    num_points = forms.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], label='Number of Charging Points')

    class Meta:
        model = ChargingStation
        fields = ['name', 'lat', 'lng', 'company', 'num_points', 'connectortype']
