from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
    <h1>inicio</h1> 
    """)

def hola_mundo(request):
    return HttpResponse("hola mundo Django")

def pagina(request):
    return HttpResponse("""
    <h1>pagina web</h1> 
    """)