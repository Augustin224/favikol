from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import  login_not_required
from django.core.mail import send_mail


@login_not_required
def home(request):
    """ 
    Fonction de rendu du home
    """
    
    context = {
        "email": settings.EMAIL_HOST_USER
    }
    return render(request, "index.html", {})




def send_contact(request):
    
    
    print("Appel de la fonction d'envoie de mail")
    """ 
    Function pour envoyer un email
    """
    send_mail(
        subject=   "Subject here",
        message=  "Here is the message.",
        recipient_list=   ["augustingalilee2@gmail.com"], 
        from_email= settings.EMAIL_HOST_USER,
        fail_silently=False,
    )
    return render(request, "index.html", {})

