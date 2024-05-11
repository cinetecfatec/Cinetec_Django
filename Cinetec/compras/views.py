from django.shortcuts import render
from  django.views.generic import TemplateView,ListView
from filmes.models import listaFilmes
from .models import Sessoes
from datetime import date

# Create your views here.

class IngressoTemplateview(TemplateView):
    template_name = "pagina-compras"

class ProgramacaoListView(ListView):
    template_name = "programacao.html"
    context_object_name = 'dados'

    def get_queryset(self):
        filmes = listaFilmes.objects.all()
        sessoes = Sessoes.objects.all()
        datas = Sessoes.objects.filter(data_sessao__gte=date.today()).values('data_sessao').distinct()
        hoje = date.today()
        data_esc = 0
        return {'filmes': filmes, 'sessoes': sessoes, 'datas': datas, 'hoje' : hoje, 'data_esc' : data_esc }

