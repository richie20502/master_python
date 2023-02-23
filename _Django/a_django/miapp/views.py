from django.shortcuts import render, HttpResponse

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
    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("hola mundo Django")

def pagina(request):
    return HttpResponse("""
    <h1>pagina web</h1> 
    """)