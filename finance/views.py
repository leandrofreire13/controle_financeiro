from django.shortcuts import render, redirect

from .models import Categoria, Gasto
from .forms import GastoForm, CategoriaForm


# Create your views here.

# GET lista todos gastos cadastrados
def listaGastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'index.html', {'gastos': gastos})

# POST cadastrar novo gasto
def cadastrarGasto(request):
    gastos = Gasto.objects.all()
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos')
    else:
        form = GastoForm()
    return render(request, 'cadastrar_gasto.html', {'form': form, 'gastos': gastos})


def cadastraCategoria(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'cadastrar_categoria.html', {'form': form, 'categorias': categorias})

