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
    <h1>inicio</h1> 
    <ul>
    """
    year=2023
    while year <= 2050:
        html +="<li>"
        html += str(year)    
        html +="</li>"
        year += 1
    
    html += "</ul>"
    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse( layout +"hola mundo Django")

def pagina(request, redirigir=0):

    if redirigir ==1:
        return redirect('/contacto/richie/recillas')
        
    return HttpResponse(layout +"""
    <h1>pagina web</h1> 
    """)

def contacto(request, nombre="nombre", ap="apellido"):
    return HttpResponse(layout + f"<h1>Contacto {nombre} {ap} </h1>")