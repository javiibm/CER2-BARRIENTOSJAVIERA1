from django.shortcuts import render
from .models import Comunicado
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def comunicados(request):
    comunicados = Comunicado.objects.all
    return render(request, 'core/comunicados.html', {'comunicados':comunicados})


def form_valid(self):
        user = User.objects.get(username = self.request.user)
        Comunicado.objects.create(publicado_por = user)
        return redirect(Comunicado)
