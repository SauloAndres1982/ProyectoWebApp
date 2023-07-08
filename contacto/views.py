from django.shortcuts import render, redirect
from .forms import FormularioContacto

def contacto(request):
    formulario_contacto = FormularioContacto(data=request.POST)

    if request.method == 'POST':
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            return redirect("/contacto/?valido")


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})