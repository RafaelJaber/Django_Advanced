# Generated by Django 2.0.1 on 2019-07-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0010_sale_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.CharField(choices=[('OP', 'Aberta'), ('CL', 'Fechada'), ('PC', 'Processando'), ('UN', 'Desconhecido')], default='UN', max_length=2, verbose_name='Status da Venda'),
        ),
    ]