
from django.urls import path
from . import views

app_name= 'travelapp'

urlpatterns = [

    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('destinations/', views.destinations, name="destinations"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),



]












