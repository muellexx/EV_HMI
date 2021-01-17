from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Company


class UserListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "settings/user_list.html"

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'User List'
        context['sidebar'] = 'Settings'
        return context


class CompanyListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "settings/company_list.html"

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['title'] = 'Company List'
        context['sidebar'] = 'Settings'
        return context
