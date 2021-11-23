from django.contrib import admin

# Register your models here.
from finance.models import Categoria, Gasto

class CampoCategoria(admin.ModelAdmin):
    list_display = ('nome',)

class CampoGasto(admin.ModelAdmin):
    list_display = ('categoria','descricao', 'valor', 'vencimento', 'status')

admin.site.register(Categoria, CampoCategoria)
admin.site.register(Gasto, CampoGasto)