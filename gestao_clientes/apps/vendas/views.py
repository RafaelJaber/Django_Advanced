import json
from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Sale, OrderItem


class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dash'):
            return HttpResponse('Acesso negado')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {}
        context['average'] = Sale.objects.average()
        context['average_discount'] = Sale.objects.discount__avg()
        context['min'] = Sale.objects.value__min()
        context['max'] = Sale.objects.value_max()
        context['count'] = Sale.objects.count_id()
        context['count_nf_submit'] = Sale.objects.count_nf_submit()
        template = 'vendas/dashboard.html'


        context['x'] = ['x', 1,2,3,4,5,6]
        context['vanda'] = ['Venda', 30, 200, 100, 400, 150, 250]
        context['data2'] = ['data2', 50, 20, 10, 40, 15, 25]
        return render(request, template, context)


class JsonView(View):

    def get(self, request):
        x = []
        venda = []
        for sale in Sale.objects.all():
            x.append(str(sale.number))
            venda.append(float(sale.value))

        dict = {
            'x': x,
            'Venda': venda
        }
        json_object = json.dumps(dict)
        return HttpResponse(json_object)
