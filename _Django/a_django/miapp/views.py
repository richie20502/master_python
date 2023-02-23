from django.shortcuts import render, HttpResponse, redirect

layout = """
    <h1>Inicio sitio</h1> 
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola">Hola </a>
        </li>
        <li>
            <a href="/pagina">Pagina</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

# Create your views here.
def index(request):
    html ="""
    
    <ul>
    """
    year=2023
    while year <= 2050:
        html +="<li>"
        html += str(year)    
        html +="</li>"
        year += 1
    
    html += "</ul>"
    return render(request, 'index.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir ==1:
        return redirect('/contacto/richie/recillas')

    return render(request,'pagina.html')

def contacto(request, nombre="nombre", ap="apellido"):
    return HttpResponse(layout + f"<h1>Contacto {nombre} {ap} </h1>")