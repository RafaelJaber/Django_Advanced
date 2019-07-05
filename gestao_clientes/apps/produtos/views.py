from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView
from .models import Product
from django.urls import reverse_lazy

"""
class ProductBulk(View):

    def get(self, request):
        products = ['banana', 'maçã', 'limão', 'Laranja', 'Pera', 'Melancia']
        list_products = []

        for product in products:
            p = Produto(descricao=product, preco=10)
            list_products.append(p)

        Produto.objects.bulk_create(list_products)
        return HttpResponse(request, 'Criado')
"""


class ProductList(ListView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = ['description', 'price']

    success_url = reverse_lazy('product_list')


class ProductDelete(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if product:
            product.delete()
        return redirect('product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['description', 'price']

    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context
