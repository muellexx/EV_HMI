from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='charger-home'),
    path('about/', views.about, name='charger-about'),
    path('dashboard/', views.dashboard, name='charger-dashboard'),
]
