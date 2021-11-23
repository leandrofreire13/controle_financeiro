from django.shortcuts import render

from .models import Categoria, Gasto
# Create your views here.

# GET lista todos gastos cadastrados
def listaGastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'index.html', {'gastos': gastos})

