from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category

layout = """
    
"""

# Create your views here.
def index(request):
    html ="""
    <ul>
    """
    year=2023
    hasta = range(year, 2050)
    while year <= 2050:
        html +="<li>"
        html += str(year)    
        html +="</li>"
        year += 1
    
    html += "</ul>"
    lenguajes =['php','js','python','java']
    return render(request, 'index.html',{
        'nombre': "nombres", 
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir ==1:
        return redirect('/contacto/richie/recillas')

    return render(request,'pagina.html', {
        'texto':'',
        'lista':['uno','dos','tres']})

def contacto(request, nombre="nombre", ap="apellido"):
    return HttpResponse(layout + f"<h1>Contacto {nombre} {ap} </h1>")


def crear_articulo(request):
    articulo = Article(
        title = "primer articulo",
        content = "contenido del articulo",
        public = True
    )
    articulo.save()
    return HttpResponse("articulo :")