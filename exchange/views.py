from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
import requests

from .models import Divisa
from .forms import DivisaForm

def get_flag_choices():
    try:
        response = requests.get("https://flagcdn.com/en/codes.json")
        response.raise_for_status()  # Raise an exception for HTTP errors
        flag_data = response.json()
        # Sort by country name for better UX
        choices = sorted([(code, name) for code, name in flag_data.items()], key=lambda x: x[1])
        choices.insert(0, ('', '-- Seleccione una bandera --'))
        return choices
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flag data: {e}")
        return [('', '-- Error al cargar banderas --')]

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
    flag_choices = get_flag_choices()
    form = DivisaForm(flag_choices=flag_choices)
    return render(request, 'exchange/divisa_list.html', {'divisas': divisas, 'form': form})

def divisa_create(request):
    flag_choices = get_flag_choices()
    if request.method == 'POST':
        form = DivisaForm(request.POST, flag_choices=flag_choices)
        if form.is_valid():
            form.save()
    return redirect('divisa_list')

def divisa_edit(request, pk):
    divisa = get_object_or_404(Divisa, pk=pk)
    flag_choices = get_flag_choices()
    if request.method == 'POST':
        form = DivisaForm(request.POST, instance=divisa, flag_choices=flag_choices)
        if form.is_valid():
            form.save()
    return redirect('divisa_list')