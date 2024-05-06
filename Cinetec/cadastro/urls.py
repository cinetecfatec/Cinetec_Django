from django.contrib import admin
from django.urls import path,include
from .views import cadastroCreateView,loginView
urlpatterns = [
    path("cadastro_novo/", cadastroCreateView.as_view(), name="pagina-cadastro"),
    path("login/", loginView.as_view(), name="pagina-login"),
]

