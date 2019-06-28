# Generated by Django 2.0.1 on 2019-06-28 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantities', models.FloatField(verbose_name='Quantidade')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Desconto')),
            ],
            options={
                'verbose_name': 'Item do Pedido',
                'verbose_name_plural': 'Itens do Pedido',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Product', verbose_name='Produto'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Sale', verbose_name='Venda'),
        ),
    ]