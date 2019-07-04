from django.conf import settings
from django.urls import path
from .views import DashboardView, JsonView, NewOrder, NewOrderItem, ListSales, EditSale

urlpatterns = [
    path('', ListSales.as_view(), name="list-sales"),
    path('novo-pedido/', NewOrder.as_view(), name="new-order"),
    path('novo-item-pedido/<int:sale>', NewOrderItem.as_view(), name="new-order-item"),
    path('editar-venda/<int:sale>', EditSale.as_view(), name="edit-order"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('dashboard-graph/', JsonView.as_view(), name="dashboard-graph"),
]
