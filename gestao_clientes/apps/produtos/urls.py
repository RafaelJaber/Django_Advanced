from django.conf import settings
from django.urls import path, include
from .views import (
    ProductList,
    ProductCreate,
    ProductDelete,
    ProductUpdate
)

urlpatterns = [
    #path('list/', persons_list, name="person_list"),
    path('', ProductList.as_view(), name="product_list"),
    path('cadastrar-produto/', ProductCreate.as_view(), name="product_create"),
    path('produto-delete/<int:pk>', ProductDelete.as_view(), name="product_delete"),
    path('produto-update/<int:pk>', ProductUpdate.as_view(), name="product_update"),
]
