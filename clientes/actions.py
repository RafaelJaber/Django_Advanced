def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)


def nfe_cancelada(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)


nfe_emitida.short_description = "NF-e emitida"
nfe_emitida.short_description = "NF-e cancelada"
