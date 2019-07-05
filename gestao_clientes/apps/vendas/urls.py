from django.conf import settings
from django.urls import path
from .views import (
    DashboardView,
    JsonView,
    NewOrder,
    NewOrderItem,
    ListSales,
    EditSale,
    DeleteSale,
    DeleteOrder,
    EditOrder,
    api,
    ViewApi
)

urlpatterns = [
    path('', ListSales.as_view(), name="list-sales"),
    path('novo-pedido/', NewOrder.as_view(), name="new-order"),
    path('novo-item-pedido/<int:sale>', NewOrderItem.as_view(), name="new-order-item"),
    path('editar-venda/<int:sale>', EditSale.as_view(), name="edit-order"),
    path('deletar-venda/<int:sale>', DeleteSale.as_view(), name="delete-sale"),
    path('deletar-order/<int:order>', DeleteOrder.as_view(), name="delete-order"),
    path('edit-order/<int:sale>/<int:order>', EditOrder.as_view(), name="edit-order-modal"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('dashboard-graph/', JsonView.as_view(), name="dashboard-graph"),
    path('api/', api, name="api"),
    path('api-view/', ViewApi.as_view(), name="api-view"),
]
