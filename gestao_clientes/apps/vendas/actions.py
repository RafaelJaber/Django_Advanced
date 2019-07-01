from django.http import HttpResponseForbidden


def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_issued=True)
    else:
        return HttpResponseForbidden()


def nfe_cancelada(modeladmin, request, queryset):
    queryset.update(nfe_issued=False)


nfe_emitida.short_description = "NF-e emitida"
nfe_emitida.short_description = "NF-e cancelada"
