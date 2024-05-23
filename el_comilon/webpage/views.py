from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def carta(request):
    context = {}
    return render(request, "pages/carta.html", context)

def locales(request):
    context = {}
    return render(request, "pages/locales.html", context)

def login(request):
    context = {}
    return render(request, "pages/login.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registro.html", context)

def reservas(request):
    context = {}
    return render(request, "pages/reservas.html", context)