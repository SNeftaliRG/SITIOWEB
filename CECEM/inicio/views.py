from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Taller

# Create your views here.
def inicioview(request):
    return render(request,"index.html")

def base (request):
    return render(request,"base.html")

def contacto (request):
    return render(request,"contacto.html")

def cursos (request):
    return render(request,"cursos.html")

def about (request):
    return render(request, "about.html")

def infocurso(request):
    return render (request,"infocurso.html")


def taller_view(request):
    talleres = Taller.objects.all().order_by('nombre')  # Asegúrate de ordenar los resultados
    paginator = Paginator(talleres, 8)  # 8 talleres por página
    page_number = request.GET.get('page')  # Obtiene el número de página
    page_obj = paginator.get_page(page_number)  # Pagina los resultados
  
    return render(request, 'talleres.html', {'page_obj': page_obj})

