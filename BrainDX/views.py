from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"BrainDX/home.html")

def about(request):
    return render(request,"BrainDX/about.html")

def team(request):
    return render(request,"BrainDX/team.html")

def services(request):
    return render(request,"BrainDX/services.html")

def contact(request):
    return render(request,"BrainDX/contact.html")

def registration(request):
    return render(request,"BrainDX/registration.html")

def login(request):
    return render(request,"BrainDX/login.html")
