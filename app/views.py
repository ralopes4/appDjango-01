from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def home(request):
    return render(request, 'app/home.html')

def adicionar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'app/adicionar_cliente.html', {'form': form})

def consultar_cliente(request):
    if 'sobrenome' in request.GET:
        sobrenome = request.GET['sobrenome']
        clientes = Cliente.objects.filter(sobrenome__icontains=sobrenome)
    else:
        clientes = None
    return render(request, 'app/consultar_cliente.html', {'clientes': clientes})
