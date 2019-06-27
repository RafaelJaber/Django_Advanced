from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .actions import nfe_emitida, nfe_cancelada


class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary', 'have_photo')
    #fields = (('doc', 'first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo')
    fieldsets = (
        ('Dados Pessoas', {'fields': (
            ('first_name', 'last_name'), 'doc')
        }),
        ('Dados Complementáres', {
            'classes': ('collapse', ),
            'fields': (
                ('age', 'salary'), 'photo', 'bio')
        })
    )
    list_filter = ('age', 'salary')
    search_fields = ('id', 'first_name', 'last_name')

    def have_photo(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    have_photo.short_description = 'Possui foto'


class SaleAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', )
    readonly_fields = ('valor', )
    actions = [nfe_emitida, nfe_cancelada]
    #raw_id_fields = ('pessoa', )
    autocomplete_fields = ['pessoa']
    list_display = ('numero', 'desconto', 'pessoa', 'total_sale', 'nfe_emitida')
    search_fields = ('numero', 'pessoa__first_name', 'pessoa__doc__num_doc')
    filter_horizontal = ['produtos']
    fieldsets = (
        ('Dados Venda', {'fields': (
            'numero', ('valor', 'desconto', 'impostos'))
        }),
        ('Dados Complementáres', {
            'classes': ('',),
            'fields': (
                ('pessoa', 'produtos'))
        })
    )

    def total_sale(self, obj):
        return obj.get_total_sale()

    total_sale.short_description = 'Total da Venda'


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, SaleAdmin)
admin.site.register(Produto)
