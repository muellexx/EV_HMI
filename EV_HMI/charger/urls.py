from django.urls import path
from . import views
from .views import ConnectorTypeCreateView

urlpatterns = [
    path('dashboard/', views.dashboard, name='charger-dashboard'),
    path('connector_type/create', ConnectorTypeCreateView.as_view(), name='connectortype-create'),
]
