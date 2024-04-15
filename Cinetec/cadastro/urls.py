from django.contrib import admin
from django.urls import path,include
from .views import cadastroCreateView
urlpatterns = [
    path("cadastro_novo/", cadastroCreateView.as_view(), name="pagina-cadastro"),
]

