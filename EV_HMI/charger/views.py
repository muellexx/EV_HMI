from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ConnectorType


def dashboard(request):
    context = {'title': 'Dashboard', 'sidebar': 'Home'}
    return render(request, 'charger/dashboard.html', context)


class ConnectorTypeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ConnectorType
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Connector Type'
        context['sidebar'] = 'Settings'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
