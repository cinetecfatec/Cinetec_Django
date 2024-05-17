from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from filmes.models import listaFilmes
from .models import Sessoes
from datetime import date,datetime
from django.shortcuts import redirect
from django.urls import reverse
from .forms import MeuForm
from django.http import HttpResponse
import ast


class IngressoTemplateview(TemplateView):
    template_name = "pagina-compras"

class ProgramacaoListView(ListView):
    template_name = "programacao.html"
    context_object_name = 'dados'

    def get_queryset(self):

        # Obtém o argumento passado na URL
        argumento = self.kwargs.get('data_esc')
        filmes = listaFilmes.objects.all()
        sessoes = Sessoes.objects.all()
        datas = Sessoes.objects.filter(data_sessao__gte=date.today()).values('data_sessao').distinct().order_by('data_sessao')
        if argumento == 'hoje':
            data_esc = datetime.now()
            data_esc = data_esc.date()
        else:
            data_esc = ast.literal_eval(argumento)
            data_esc = data_esc['data_esc']
            data_esc = datetime.strptime(data_esc,"%d de %B de %Y")
            data_esc = data_esc.date()

        return {'filmes': filmes, 'sessoes': sessoes, 'datas': datas, 'data_esc': data_esc}


class DataEscolhidaView(TemplateView):
    template_name = "data_escolhida"

    def dispatch(self, request, *args, **kwargs):
        # Check if the cookie exists in the request
        data_from_cookie = request.COOKIES.get('data_esc')
        if data_from_cookie:
            print(data_from_cookie)
            print(type(data_from_cookie))
        else:
            print('No data found in cookie.')
        # Continue with the normal dispatch process
        return redirect('pagina-programacao',{'data_esc':data_from_cookie})

class CompraDetailView(DetailView):
    model = listaFilmes    
    template_name = "Compra.html"