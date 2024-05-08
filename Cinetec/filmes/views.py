from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from  django.views.generic import TemplateView,DetailView
from .models import listaFilmes
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.{% endblock %}


class indexListView(ListView):
        template_name = "index.html"
        queryset = listaFilmes.objects.all()
        context_object_name = 'filmes'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.user.is_authenticated:
                context["user"] = self.request.user.get_full_name()
            return context
        

class programacaoListView(ListView):
    template_name = "programacao.html"
    queryset = listaFilmes.objects.all()
    context_object_name = 'filmes'
    


class sobreView(TemplateView):
    template_name = "sobre_nos.html"

class escolhidoDetailView(DetailView):
    model = listaFilmes    
    template_name = "escolhido.html"




