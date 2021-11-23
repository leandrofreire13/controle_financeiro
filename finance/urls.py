from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaGastos, name="gastos" )
]