from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaGastos, name="gastos" ),
    path('cadastrar', views.cadastrarGasto, name="cadastrar_gastos" )
]