from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import Formulario
#from django.contrib.auth.forms import UserRegisterForm
# Create your views here.

def index(request):
    
    if request.method == "POST":
        form = Formulario(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")        
            message = form.cleaned_data.get("message")

            success = send_mail(subject, f"{name} - {email} \n\n {message}", "gyser.django@gmail.com",["gyser.world@gmail.com"], fail_silently=False)
        
            if success:
                messages.success(request, 'El mensaje se envió correctamente')
            
        else:
            messages.warning(request, 'Error al enviar el mensaje.')
        
        return redirect("index")
    form = Formulario
    return render(request, "core/index.html", {'form':form})



def indexx(request):
    
    if request.method == "POST":
        if request.POST['subject'] and request.POST["name"] and request.POST["email"] and request.POST["message"]:
            subject = request.POST['subject']
            name = request.POST["name"]
            email = request.POST["email"]        
            message = request.POST["message"]

            success = send_mail(subject, f"{name} - {email} \n\n {message}", "gyser.django@gmail.com",["gyser.world@gmail.com"], fail_silently=False)
        
            if success:
                messages.success(request, 'El mensaje se envió correctamente')
            
        else:
            messages.warning(request, 'Error al enviar el mensaje.')
        
        return redirect("index")
    
    return render(request, "core/index.html", )
