# Generated by Django 2.0.1 on 2019-06-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Total R$'),
        ),
    ]
