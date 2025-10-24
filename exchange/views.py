from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
import requests
from django.contrib.staticfiles.storage import staticfiles_storage

from .models import Divisa
from .forms import DivisaForm

def get_flag_choices():
    import logging
    logger = logging.getLogger(__name__)
    try:
        response = requests.get("https://flagcdn.com/en/codes.json")
        response.raise_for_status()  # Raise an exception for HTTP errors
        flag_data = response.json()
        # Sort by country name for better UX
        choices = sorted([(code, name) for code, name in flag_data.items()], key=lambda x: x[1])
        choices_with_urls = []
        choices_with_urls.insert(0, ('', '-- Seleccione una bandera --', ''))
        for code, name in choices:
            if code:
                # Construct proxy URL for the flag
                flag_url = f'/flags/proxy/{code}.svg'
                choices_with_urls.append((code, name, flag_url))
            else:
                choices_with_urls.append((code, name, ''))
        logger.info("Successfully fetched flag data.")
        return choices_with_urls
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching flag data: {e}")
        return [('', '-- Error al cargar banderas --', '')]

def flag_proxy(request, flag_code):
    try:
        flag_url = f"https://flagcdn.com/w20/{flag_code}.png" # Using w20 for smaller size and png for broader support
        response = requests.get(flag_url, stream=True)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', 'image/png')
        return HttpResponse(response.content, content_type=content_type)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error fetching flag: {e}", status=500, content_type="text/plain")

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
    flag_choices_data = get_flag_choices()
    form = DivisaForm()
    return render(request, 'exchange/divisa_list.html', {'divisas': divisas, 'form': form, 'flag_choices': flag_choices_data})

def divisa_create(request):
    flag_choices_data = get_flag_choices()
    if request.method == 'POST':
        form = DivisaForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('divisa_list')

def divisa_edit(request, pk):
    divisa = get_object_or_404(Divisa, pk=pk)
    flag_choices_data = get_flag_choices()
    if request.method == 'POST':
        form = DivisaForm(request.POST, instance=divisa)
        if form.is_valid():
            form.save()
    return redirect('divisa_list')