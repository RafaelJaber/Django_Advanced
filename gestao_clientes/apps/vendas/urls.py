from django.conf import settings
from django.urls import path
from .views import DashboardView, JsonView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('dashboard-graph/', JsonView.as_view(), name="dashboard-graph"),
]
