# Generated by Django 2.0.1 on 2019-06-28 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20190627_2153'),
        ('vendas', '0003_auto_20190627_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantities', models.FloatField(verbose_name='Quantidade')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Desconto')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Product', verbose_name='Produto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='vendas.Sale', verbose_name='Venda')),
            ],
            options={
                'verbose_name': 'Item do Pedido',
                'verbose_name_plural': 'Itens do Pedido',
            },
        ),
    ]
