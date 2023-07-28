from django.urls import path
from . import views
urlpatterns = [

    path("",views.home,name="home"),
    path("about", views.about, name="about"),
    path("team", views.team, name="team"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),

]
