from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ConnectorType, ChargingStation, ChargingPoint, Connector
from .forms import ChargingStationForm


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
        context['title'] = 'Create Connector Type'
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

        print(charging_station.num_points)
        print(form.cleaned_data['connectortype'])
        return HttpResponseRedirect(self.model.get_absolute_url(charging_station))


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

