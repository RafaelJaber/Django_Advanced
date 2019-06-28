from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import View

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

