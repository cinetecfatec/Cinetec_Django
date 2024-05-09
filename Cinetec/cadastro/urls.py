from django.contrib import admin
from django.urls import path,include
from .views import  cadastroCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cadastro_novo/", cadastroCreateView.as_view(), name="pagina-cadastro"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='pagina-login'),
    path('logout/', auth_views.LogoutView.as_view(method = "POST"), name='pagina-logout'),
]

