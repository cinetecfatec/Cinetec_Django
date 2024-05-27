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
import json


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
    template_name = "data_escolhida.html"
    
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
    
    
class IngressoEscolhidoView(TemplateView):
    template_name = "checkout.html"
    
    def post(self,request,*args, **kwargs):
            meu_dado = request.POST.get
            return super().get(request,*args, **kwargs)

class CompraListView(ListView):
    template_name = "Compra.html"
    context_object_name = 'dados'    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context
        
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        sessoes = Sessoes.objects.all()
        sessao = Sessoes.objects.filter(Id_sessao = pk)
        filmes = listaFilmes.objects.all()
        sessao_assentos = Sessoes.objects.get(Id_sessao=pk)
        # assentos = sessao_assentos.assentos  # Fetch the 'assentos' field value
        assentos = 'e' * 50 + 'o' * 78

        return {'filmes': filmes, 'sessoes': sessoes, 'pk': pk, 'sessao':sessao, 'assentos': assentos }
    
class CheckoutListview(ListView):
    template_name = "checkout.html"
    context_object_name = 'dados'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assentos_check'] = self.kwargs.get('assentos_check')
        return context

    def get_queryset(self):
        pk = self.kwargs.get('assentos_check')
        sessoes = Sessoes.objects.all()
        sessao = Sessoes.objects.filter(Id_sessao = pk)
        filmes = listaFilmes.objects.all()
        sessao_assentos = Sessoes.objects.get(Id_sessao=pk)
        assentos = sessao_assentos.assentos  # Fetch the 'assentos' field value

        return {'filmes': filmes, 'sessoes': sessoes, 'pk': pk, 'sessao':sessao, 'assentos': assentos }