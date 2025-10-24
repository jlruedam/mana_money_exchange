from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Divisa

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