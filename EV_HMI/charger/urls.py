from django.urls import path
from . import views
from .views import ConnectorTypeCreateView, ConnectorTypeDetailView

urlpatterns = [
    path('dashboard/', views.dashboard, name='charger-dashboard'),
    path('connector_type/create/', ConnectorTypeCreateView.as_view(), name='connectortype-create'),
    path('connector_type/<int:pk>/', ConnectorTypeDetailView.as_view(), name='connectortype-create'),
]
