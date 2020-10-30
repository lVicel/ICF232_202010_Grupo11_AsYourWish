from django.shortcuts import render, redirect
from .forms import ResidenciasForm

def selResidencia(request):
    context = {}
    form = ResidenciasForm()
    context['form'] = form
    if request.GET:
        temp = request.GET['residencias_field']
        print(temp)
        return redirect('/')
    return render(request, "Selección_Residencia.html", context)

# Create your views here.
