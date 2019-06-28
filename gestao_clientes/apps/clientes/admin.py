from django.contrib import admin
from .models import Person, Documento


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


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)

