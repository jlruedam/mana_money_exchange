from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from .models import Divisa
from .forms import DivisaForm

def index(request):
    divisas = Divisa.objects.all()
    return render(request, 'exchange/index.html', {'divisas': divisas})

def calculate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data['action']
        currency = data['currency']
        amount = float(data['amount'])

        divisa = Divisa.objects.get(nombre=currency)
        if action == 'Comprar':
            result = amount * float(divisa.compra)
        else:
            result = amount * float(divisa.venta)
        
        return JsonResponse({'result': result})

def tv_view(request):
    divisas = Divisa.objects.all()
    return render(request, 'exchange/tv-view.html', {'divisas': divisas})

def divisa_list(request):
    divisas = Divisa.objects.all()
    return render(request, 'exchange/divisa_list.html', {'divisas': divisas})

def divisa_create(request):
    if request.method == 'POST':
        form = DivisaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('divisa_list')
    else:
        form = DivisaForm()
    return render(request, 'exchange/divisa_form.html', {'form': form})

def divisa_edit(request, pk):
    divisa = get_object_or_404(Divisa, pk=pk)
    if request.method == 'POST':
        form = DivisaForm(request.POST, instance=divisa)
        if form.is_valid():
            form.save()
            return redirect('divisa_.list')
    else:
        form = DivisaForm(instance=divisa)
    return render(request, 'exchange/divisa_form.html', {'form': form})