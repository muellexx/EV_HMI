from django.urls import path
from . import views
from .views import ConnectorTypeCreateView, ConnectorTypeDetailView, ConnectorTypeListView, ChargingStationCreateView, ChargingStationDetailView, ChargingStationListView

urlpatterns = [
    path('dashboard/', views.dashboard, name='charger-dashboard'),
    path('connector_type/create/', ConnectorTypeCreateView.as_view(), name='connectortype-create'),
    path('connector_type/', ConnectorTypeListView.as_view(), name='connectortype-list'),
    path('connector_type/<int:pk>/', ConnectorTypeDetailView.as_view(), name='connectortype-detail'),
    path('charging_station/create/', ChargingStationCreateView.as_view(), name='chargingstation-create'),
    path('charging_station/', ChargingStationListView.as_view(), name='chargingstation-list'),
    path('charging_station/<int:pk>/', ChargingStationDetailView.as_view(), name='chargingstation-detail'),
]
