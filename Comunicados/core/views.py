from django.shortcuts import render
from .models import Comunicado

# Create your views here.
def comunicados(request):
    comunicados = Comunicado.objects.all
    return render(request, 'core/comunicados.html', {'comunicados':comunicados})
#pendiente
def nuevo_comunicado(request):
    if request.POST:
        titulo= request.POST['titulo']
        c = Comunicado()
        c.save()
        return redirect(comunicado)
    return render(request, 'core/nuevo_comunicado.html')

def nuevo_usuario(request):
    if request.POST:
        nombre= request.POST['nombre']
        apellido= request.POST['apellido']
        email= request.POST['email']
        d = Docente(nombre=nombre,apellido=apellido,email=email)
        d.save()
        return redirect(docentes)
    return render(request, 'core/nuevo_docente.html')