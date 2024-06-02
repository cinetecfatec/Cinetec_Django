from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from filmes.models import listaFilmes
from .models import Sessoes,Tabela_preco
from datetime import date,datetime
from django.shortcuts import redirect
from django.urls import reverse
from .forms import MeuForm
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import ast
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,re


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
        assentos = sessao_assentos.assentos  # Fetch the 'assentos' field value
        #assentos = 'e' * 50 + 'o' * 78

        return {'filmes': filmes, 'sessoes': sessoes, 'pk': pk, 'sessao':sessao, 'assentos': assentos }

class IngressoEscolhidoView(TemplateView):
    template_name = "IngressoEscolhido.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = json.loads(request.body)
            # Processar os dados recebidos
            print(data)
            # Acessando dados específicos
            sessao_id = data.get('sessao')
            cadeiras_selecionadas = data.get('cadeiras_selecionadas', [])

            # Extrair os números das strings e converter para inteiros
            cadeiras_numeros = [int(re.search(r'\d+', cadeira).group()) for cadeira in cadeiras_selecionadas]
            
            print("Sessão ID:", sessao_id)
            print("Cadeiras Selecionadas:", cadeiras_selecionadas)
            print("Cadeiras Números:", cadeiras_numeros)
                # Cria uma resposta HTTP
            response = HttpResponse('pagina-checkout')
            # Define cookies na resposta
            response.set_cookie('sessao_id', sessao_id, httponly=True, secure=True)
            response.set_cookie('cadeiras_numeros', json.dumps(cadeiras_numeros), httponly=True, secure=True)

            return response

class CheckoutListview(ListView):
    template_name = "checkout.html"
    context_object_name = 'dados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessao_id'] = self.request.COOKIES.get('sessao_id')
        context['cadeiras_numeros'] = json.loads(self.request.COOKIES.get('cadeiras_numeros', '[]'))  # Convertendo de volta para lista
        return context
    
    def get_queryset(self):
        pk = int( self.request.COOKIES.get('sessao_id'))
        sessoes = Sessoes.objects.all()
        sessao = Sessoes.objects.filter(Id_sessao = pk).values('Id_sessao', 'Id_filme_id','sala','assentos')
        sessao_atual = sessao[0]
        filme_atual = sessao_atual['Id_filme_id']
        assentos_banco = sessao_atual['assentos']
        filmes = listaFilmes.objects.filter(id_filme = filme_atual).values('nome_filme')
        filme_escolhido = filmes[0]
        sala = sessao_atual['sala']
        filme = filme_escolhido['nome_filme']
        
        
        # assentos = sessao.assentos  # Fetch the 'assentos' field value
        assentos_escolhidos =  json.loads(self.request.COOKIES.get('cadeiras_numeros', '[]')) 
        
        preco = Tabela_preco.objects.all()
        ingressos = Tabela_preco.objects.filter(tipo = 'ingresso').values('descricao','preco')
        inteira = ingressos[0]
        inteira = inteira['preco']
        meia = ingressos[1]
        meia = meia['preco']
        vip = ingressos[2]
        vip = vip['preco']

        return {'inteira': inteira, 'meia': meia, 'vip': vip, 'preco': preco, 'filmes': filmes, 'sala': sala, 'filme': filme, 'sessoes': sessoes, 'pk': pk, 'assentos_escolhidos': assentos_escolhidos, 'sessao':sessao }