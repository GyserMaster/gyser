from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import Formulario
from django.conf import settings

import urllib
import json
#from django.contrib.auth.forms import UserRegisterForm
# Create your views here.

def portfolio(request):
    
    if request.method == "POST":
        myform = Formulario(request.POST)

        if myform.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = "https://www.google.com/recaptcha/api/siteverify"
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }

            subject = myform.cleaned_data.get('subject')
            name = myform.cleaned_data.get("name")
            email = myform.cleaned_data.get("email")
            message = myform.cleaned_data.get("message")

            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                send_mail(subject, f"{name} - {email} \n\n {message}", "gyser.django@gmail.com",["gyser.world@gmail.com"], fail_silently=False)
                messages.success(request, 'El mensaje se envió correctamente')
            
            else:
                messages.error(request, 'Error al enviar el mensaje, active el captcha')
        
            return redirect("portfolio")

    myform = Formulario
    return render(request, "portfolio/gyser.html", {'form':myform})
