from django.shortcuts import render
from django.views.generic import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Sale, OrderItem


class DashboardView(View):

    def get(self, request):
        context = {}
        context['average'] = Sale.objects.all().aggregate(
            Avg('value')
        )['value__avg']
        context['average_discount'] = Sale.objects.all().aggregate(
            Avg('discount')
        )['discount__avg']
        context['min'] = Sale.objects.all().aggregate(
            Min('value')
        )['value__min']
        context['max'] = Sale.objects.all().aggregate(
            Max('value')
        )['value__max']
        context['count'] = Sale.objects.all().aggregate(
            Count('id')
        )['id__count']
        context['count_nf_submit'] = Sale.objects.filter(nfe_issued=True).aggregate(
            Count('id')
        )['id__count']
        template = 'vendas/dashboard.html'
        return render(request, template, context)
