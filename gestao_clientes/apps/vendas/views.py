import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View, ListView
from .models import Sale, OrderItem
from .forms import OrderItemForm


class ListSales(ListView):
    model = Sale
    template_name = 'vendas/list_sales.html'


class NewOrder(View):
    def get(self, request):
        template = 'vendas/new-order.html'
        return render(request, template)

    def post(self, request):
        data = {}
        data['numero'] = int(request.POST['numero'])
        data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
        data['venda'] = request.POST['venda_id']

        if data['venda']:
            venda = Sale.objects.get(id=data['venda'])
            venda.discount = data['desconto']
            venda.number = data['numero']
            venda.save()
        else:
            venda = Sale.objects.create(
                number=data['numero'],
                discount=data['desconto']
            )

        itens = venda.orderitem_set.all()
        data['venda_obj'] = venda
        data['itens'] = itens
        data['form_item'] = OrderItemForm()

        template = 'vendas/new-order.html'
        return render(request, template, data)


class NewOrderItem(View):
    def get(self, request, pk):
        return HttpResponse('Rafael Dando Manota')

    def post(self, request, sale):
        data = {}
        item = OrderItem.objects.create(
            product_id=request.POST['product_id'], quantities=request.POST['quantity'],
            discount=request.POST['discount'], sale_id=sale
        )
        data['item'] = item
        data['form_item'] = OrderItemForm()
        data['numero'] = item.sale.number
        data['desconto'] = item.sale.discount
        data['venda'] = item.sale.id
        data['venda_obj'] = item.sale
        data['itens'] = item.sale.orderitem_set.all()

        return render(
            request, 'vendas/new-order.html', data
        )


class EditSale(View):
    def get(self, request, sale):
        sale = get_object_or_404(Sale, id=sale)
        data = {}
        data['form_item'] = OrderItemForm()
        data['numero'] = sale.number
        data['desconto'] = float(sale.discount)
        data['venda'] = sale.id
        data['venda_obj'] = sale
        data['itens'] = sale.orderitem_set.all()

        return render(
            request,  'vendas/new-order.html', data
        )


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
