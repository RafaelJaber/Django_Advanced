from django.contrib import admin
from .models import Sale
from .actions import *
from .models import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class SaleAdmin(admin.ModelAdmin):
    list_filter = ('person__doc', )
    readonly_fields = ('value', )
    actions = [nfe_emitida, nfe_cancelada]
    #raw_id_fields = ('person', )
    autocomplete_fields = ['person']
    list_display = ('number', 'discount', 'person', 'value', 'nfe_issued', 'status')
    search_fields = ('number', 'person__first_name', 'person__doc__num_doc')
    fieldsets = (
        ('Dados Venda', {'fields': (
            'number', ('value', 'discount', 'taxes', 'status'))
        }),
        ('Dados Complementáres', {
            'classes': ('',),
            'fields': (
                ('person', ))
        })
    )
    inlines = [OrderItemInline]


admin.site.register(Sale, SaleAdmin)
admin.site.register(OrderItem)
