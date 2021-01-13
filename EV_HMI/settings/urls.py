from django.urls import path
from .views import UserListView, CompanyListView
from . import views

urlpatterns = [
    path('', UserListView.as_view(), name='settings-user-list'),
    path('companies/', CompanyListView.as_view(), name='settings-company-list'),
]
