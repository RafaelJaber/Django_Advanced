# Generated by Django 2.0.1 on 2019-06-27 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_venda_nfe_emitida'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantities', models.FloatField(verbose_name='Quantidade')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Produto', verbose_name='Produto')),
            ],
        ),
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Venda', verbose_name='Venda'),
        ),
    ]