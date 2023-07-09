from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = FormularioContacto(data=request.POST)

    if request.method == 'POST':
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django", "El usuario con nombre {} con dirección {} escribe lo siguiente: \n\n{}".format(nombre, email, contenido),"",["saulocarmonatoro@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})