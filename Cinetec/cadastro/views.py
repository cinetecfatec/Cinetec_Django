from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import NovoCadastro


# Create your views here.

class cadastroCreateView(CreateView):
    model = User
    form_class = NovoCadastro
    template_name = "cadastroNovo.html"
    success_url = reverse_lazy('pagina-inicio')