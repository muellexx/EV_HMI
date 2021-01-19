from django.urls import path
from .views import UserListView, CompanyListView
from . import views

urlpatterns = [
    path('user_list/', UserListView.as_view(), name='settings-user-list'),
    path('company_list/', CompanyListView.as_view(), name='settings-company-list'),
]
