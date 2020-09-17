from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import Formulario
from django.conf import settings

import urllib
import json
#from django.contrib.auth.forms import UserRegisterForm
# Create your views here.

def index(request):
    
    if request.method == "POST":
        form = Formulario(request.POST)

        if form.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = "https://www.google.com/recaptcha/api/siteverify"
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }

            subject = form.cleaned_data.get('subject')
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")        
            message = form.cleaned_data.get("message")

            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                send_mail(subject, f"{name} - {email} \n\n {message}", "gyser.django@gmail.com",["gyser.world@gmail.com"], fail_silently=False)
                messages.success(request, 'El mensaje se envió correctamente')
            
            else:
                messages.error(request, 'Error al enviar el mensaje, active el captcha')
        
            return redirect("index")

    form = Formulario
    return render(request, "core/index.html", {'form':form})


def projects(request):
    return render(request, "core/projects.html")