from django import forms
from .models import ChargingStation, ConnectorType


class ChargingStationForm(forms.ModelForm):
    connectortype = forms.ModelMultipleChoiceField(queryset=ConnectorType.objects.all())

    class Meta:
        model = ChargingStation
        fields = ['name', 'lat', 'lng', 'company', 'num_points', 'connectortype']
