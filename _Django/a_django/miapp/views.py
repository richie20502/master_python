from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle

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
    #articulos = Article.objects.order_by('-id')[:3]
    #articulos = Article.objects.filter(title='Batman',id=2)
    #en el title contenga articulo 
    #articulos = Article.objects.filter(title__contains="articulo")

    #en el title contenga exactamente articulo
    #articulos = Article.objects.filter(title__exact="articulo")

    #en el id gt=graden than contenga mayor al id
    #articulos = Article.objects.filter(id__gt=10)

    #en el id gte=graden than igual contenga mayor  o igual  que id
    #articulos = Article.objects.filter(id__gte=10)

    #en el id lt= menores que id
    #articulos = Article.objects.filter(id__lt=10)

    #en el id lt= menores he iguales que id
    #articulos = Article.objects.filter(id__lte=10)

    #articulos = Article.objects.filter(id=1).exclude(public=True)

    #articulos = Article.objects.raw('SELECT * FROM miapp_article')

    """ 
    articulos = Article.objects.filter(
        Q(title__contains='') | Q(title__contains='')
    )
    """

    return render(request,'articulos.html',{
        'articulos': articulos
    })
    return HttpResponse()

def borrar_articulos(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def save_article(request):
    if request.method == 'POST':
        articulo = Article(
            title = request.POST['title'],
            content = request.POST['content'],
            public = request.POST['public']
            )
        articulo.save()
        return HttpResponse(f"Articulo creado : {articulo.title}")
    else:
        return HttpResponse("<h2> no se pude crear articulo </h2>")

def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = request.POST['title'],
                content = request.POST['content'],
                public = request.POST['public'])
            articulo.save()
            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request,'create_full_article.html',{
        'form' : formulario
    })
