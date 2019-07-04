from django import forms


class OrderItemForm(forms.Form):
    product_id = forms.CharField(label='ID do Produto', max_length=100)
    quantity = forms.IntegerField(label='Quantidade')
    discount = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)
