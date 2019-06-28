from django.shortcuts import render
from django.views.generic import View
from .models import Sale, OrderItem


class DashboardView(View):

    def get(self, request):
        context = {}
        context['average'] = Sale.objects.average()
        context['average_discount'] = Sale.objects.discount__avg()
        context['min'] = Sale.objects.value__min()
        context['max'] = Sale.objects.value_max()
        context['count'] = Sale.objects.count_id()
        context['count_nf_submit'] = Sale.objects.count_nf_submit()
        template = 'vendas/dashboard.html'
        return render(request, template, context)
