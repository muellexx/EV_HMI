from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ConnectorType, ChargingStation, ChargingPoint, Connector
from .forms import ChargingStationForm
from map.utils import json_stations


def dashboard(request):
    context = {'title': 'Dashboard', 'sidebar': 'Home'}
    return render(request, 'charger/dashboard.html', context)


class ConnectorTypeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ConnectorType
    fields = ['name', 'dc_charging']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Connector Type'
        context['sidebar'] = 'Settings'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ConnectorTypeListView(ListView):
    model = ConnectorType
    context_object_name = 'connectortypes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Connector Type'
        context['sidebar'] = 'Settings'
        return context


class ConnectorTypeDetailView(DetailView):
    model = ConnectorType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Connector Type'
        context['sidebar'] = 'Settings'
        return context


class ChargingStationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ChargingStationForm
    model = ChargingStation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Charging Station'
        context['sidebar'] = 'Settings'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        charging_station = form.save()
        connector_types = form.cleaned_data['connectortype']
        for i in range(form.cleaned_data['num_points']):
            point = ChargingPoint(station=charging_station, point_id=i)
            point.save()
            for j, connector_type in enumerate(connector_types):
                connector = Connector(charging_point=point, connector_type=connector_type, connector_id=j)
                connector.save()

        return HttpResponseRedirect(self.model.get_absolute_url(charging_station))


class ChargingStationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ChargingStation
    fields = ['name', 'lat', 'lng', 'company']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Charging Station'
        context['sidebar'] = 'Settings'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        redirect_url = super().form_valid(form)
        json_stations()
        return redirect_url


class ChargingStationListView(ListView):
    model = ChargingStation
    context_object_name = 'chargingstations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Charging Stations'
        context['sidebar'] = 'Settings'
        return context


class ChargingStationDetailView(DetailView):
    model = ChargingStation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Charging Station'
        context['sidebar'] = 'Settings'
        return context

