from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Accounts

def register(request:HttpRequest):
    if request.method =="POST":
        
        new_user = Accounts(
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            email = request.POST.get("email"),
            pasword = request.POST.get("password"),
            pasword_test = request.POST.get("password_test"),
            rol = request.POST.get("rol")
        )

        if request.POST.get("pasword") == request.POST.get("pasword_test"):
            new_user.save()
            return redirect("bosh sahifa")
        

        return render(request=request, template_name="register.html")


    return render(request=request, template_name="register.html")

def login(request:HttpRequest)->HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email")
        pasword = request.POST.get("pasword")
        rol = request.POST.get("rol")
        try:
            user = Accounts.objects.get(email=email, pasword=pasword, rol=rol)

            return HttpResponse("bosh sahifaga xush kelibsiz")
    
        except Accounts.DoesNotExist:
        
            return HttpResponse("xatolik mavjud iltimos malumotlarni togri kiriting !!!")
    
    return render(request=request, template_name="login.html")
    

