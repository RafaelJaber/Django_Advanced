import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import View, ListView
from .models import Sale, OrderItem
from .forms import OrderItemForm, OrderForm
from django.contrib import messages
from gestao_clientes.apps.produtos.models import Product
from django.forms import model_to_dict


class ListSales(ListView):
    model = Sale
    template_name = 'vendas/list_sales.html'


class NewOrder(View):
    def get(self, request):
        template = 'vendas/new-order.html'
        return render(request, template)

    def post(self, request):
        data = {}
        data['numero'] = int(request.POST['numero'].replace(',', '.'))
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

        if OrderItem.objects.filter(product_id=request.POST['product_id'], sale_id=sale).exists():
            item = get_object_or_404(OrderItem, product_id=request.POST['product_id'], sale_id=sale)
            print(item)
            item.quantities = item.quantities + 1
            item.save()
            data['item'] = item
        else:
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
        messages.success(
            self.request, 'Item adicionado'
        )
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


class DeleteSale(View):
    def get(self, request, sale):
        delete = get_object_or_404(Sale, id=sale)
        if delete:
            delete.delete()
            messages.success(
                request, 'Venda deletada'
            )
        return redirect('list-sales')


class DeleteOrder(View):
    def get(self, request, order):
        order = get_object_or_404(OrderItem, id=order)
        if order:
            order.delete()
            messages.success(
                request, 'Item Deletado'
            )
        return redirect('new-order')


class EditOrder(View):
    def get(self, request, sale, order):

        sale = get_object_or_404(Sale, id=sale)
        data = {}
        data['form_item'] = OrderItemForm()
        data['numero'] = sale.number
        data['desconto'] = float(sale.discount)
        data['venda'] = sale.id
        data['venda_obj'] = sale
        data['itens'] = sale.orderitem_set.all()

        edit = get_object_or_404(OrderItem, id=order)
        data['itemName'] = edit.product.description
        data['formItem'] = OrderForm(instance=edit)

        data['csrf_token_value'] = request.COOKIES['csrftoken']
        return HttpResponse(
            render_to_string('vendas/order-edit.html', data)
        )

    def post(self, request, order, sale, *args, **kwargs):
        quantity = request.POST['quantities']
        discount = request.POST['discount']
        item = get_object_or_404(OrderItem, id=order)
        if item:
            quantity = quantity.split('.')[0]
            item.quantities = int(quantity.replace(',', '.'))
            item.discount = float(discount.replace(',', '.'))
            item.save()
            messages.success(
                self.request, 'Item atualizado'
            )
            return redirect('edit-order', sale)


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


def api(request):
    l = []
    produtos = Product.objects.all()
    for produto in produtos:
        l.append(model_to_dict(produto))
    return JsonResponse(l, status=200, safe=False)


class ViewApi(View):
    def get(self, request):
        data = {'nome': 'Rafael'}
        produtos = Product.objects.all()
        l = []
        for produto in produtos:
            l.append(model_to_dict(produto))

        return JsonResponse(l, safe=False)
