from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "generator/home.html", {"message": "Hello Welcome!"})


def password(request):
    charactors = list("abcdefghijklmnopkrstuvwxyz")
    length = int(request.GET.get("length"))
    if request.GET.get("Uppercase"):
        charactors.extend(list("abcdefghijklmnopkrstuvwxyz".upper()))

    if request.GET.get("Special"):
        charactors.extend(list("~!@#$%^&*()<>?"))

    if request.GET.get("Numbers"):
        charactors.extend(list("0123456789"))

    thepassword = ""
    for i in range(length):
        thepassword += random.choice(charactors)

    return render(request, "generator/password.html", {"password":thepassword})

def about(request):
    return render(request, "generator/about.html")