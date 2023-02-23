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


def crear_articulo(request,title,content,public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado : {articulo.title}")

def articulo(request):
    try:
        articulo = Article.objects.get(pk=1)
        response = f"Articulo: {articulo.title}"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)

def editar_articulo(request, id):
    print(f"el id es {id}")
    articulo = Article.objects.get(pk=id)
    articulo.title = 'titulo modificado'
    articulo.content = 'contenido modificado'
    articulo.public = True

    articulo.save()
    return HttpResponse(f"Articulo editado : {articulo.title}")

def articulos(request):
    articulos = Article.objects.all()
    articulos = Article.objects.order_by('-id')[:3]
    return render(request,'articulos.html',{
        'articulos': articulos
    })
    return HttpResponse()

