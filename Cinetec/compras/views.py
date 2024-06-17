from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView, ListView
from filmes.models import listaFilmes
from .models import Sessoes, Tabela_preco
from datetime import date, datetime
from django.http import HttpResponse
import ast
import json
import re


class ProgramacaoListView(ListView):
    template_name = "programacao.html"
    context_object_name = 'dados'

    def get_queryset(self):
        argumento = self.kwargs.get('data_esc')
        filmes = listaFilmes.objects.all()
        sessoes = Sessoes.objects.all()
        datas = Sessoes.objects.filter(data_sessao__gte=date.today()).values('data_sessao').distinct().order_by('data_sessao')
        if argumento == 'hoje':
            data_esc = datetime.now().date()
        else:
            data_esc = ast.literal_eval(argumento)['data_esc']
            data_esc = datetime.strptime(data_esc, "%d de %B de %Y").date()

        return {'filmes': filmes, 'sessoes': sessoes, 'datas': datas, 'data_esc': data_esc}

class DataEscolhidaView(TemplateView):
    template_name = "data_escolhida.html"
    
    def dispatch(self, request, *args, **kwargs):
        data_from_cookie = request.COOKIES.get('data_esc')
        if data_from_cookie:
            return redirect('pagina-programacao', {'data_esc': data_from_cookie})
        return redirect('pagina-programacao')

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
        sessao = Sessoes.objects.filter(Id_sessao=pk)
        filmes = listaFilmes.objects.all()
        sessao_assentos = Sessoes.objects.get(Id_sessao=pk)
        assentos = sessao_assentos.assentos

        return {'filmes': filmes, 'sessoes': sessoes, 'pk': pk, 'sessao': sessao, 'assentos': assentos}

class IngressoEscolhidoView(TemplateView):
    template_name = "IngressoEscolhido.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = json.loads(request.body)
            sessao_id = data.get('sessao')
            cadeiras_selecionadas = data.get('cadeiras_selecionadas', [])

            cadeiras_numeros = [int(re.search(r'\d+', cadeira).group()) for cadeira in cadeiras_selecionadas]

            response = HttpResponse('pagina-checkout')
            response.set_cookie('sessao_id', sessao_id, httponly=True, secure=True)
            response.set_cookie('cadeiras_numeros', json.dumps(cadeiras_numeros), httponly=True, secure=True)

            return response

class CheckoutListview(ListView):
    template_name = "checkout.html"
    context_object_name = 'dados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessao_id'] = self.request.COOKIES.get('sessao_id')
        context['cadeiras_numeros'] = json.loads(self.request.COOKIES.get('cadeiras_numeros', '[]'))
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

        return {
            'inteira': inteira, 'meia': meia, 'vip': vip, 'preco': preco,
            'filmes': filmes, 'sala': sala, 'filme': filme, 'sessoes': sessoes, 
            'pk': pk, 'assentos_escolhidos': assentos_escolhidos, 'sessao':sessao 
            }

from django.shortcuts import render, redirect, get_object_or_404
from .models import Sessoes

def finalizar_compra(request):
    if request.method == 'POST':
        # Supondo que o ID da sessão seja enviado no POST
        sessao_id = request.POST.get('sessao_id')
        sessao_assentos = request.POST.get('sessao_assentos')
        sessao_banco = Sessoes.objects.filter(Id_sessao = sessao_id).values('assentos')
        lista_assento = sessao_banco[0]
        lista_assento = lista_assento['assentos']
        lista_assento = list(lista_assento)
        
        if sessao_id:
            sessao = get_object_or_404(Sessoes, pk=sessao_id)
            assentos_atualizados = list(sessao.assentos)
            indice = None
            # # Itera sobre os assentos submetidos pelo usuário
            for assento in sessao_assentos:
                if assento.isdigit():  # Verifica se todos os caracteres são dígitos
                    if indice == None:
                        indice = int(assento)
                    else:
                        indice = (indice * 10) + int(assento)
                else :
                    if indice != None:
                        lista_assento[indice] = 'o'
                        indice = None
                    
            print(indice)   
            print(type(indice))
            lista_assento = ''.join(lista_assento)

            # Aqui você pode fazer qualquer validação ou processamento adicional
            # antes de salvar os assentos atualizados no banco de dados.

            # Atualiza a sessão com os novos assentos
            
            sessao.assentos = lista_assento
            sessao.save()

            return redirect('pagina-inicio')
        else:
            # Se não houver sessao_id no POST, faça o tratamento adequado (redirecionamento, mensagem de erro, etc.)
            return redirect('pagina-programacao')

    # Se o método da requisição não for POST, redireciona ou retorna uma página de erro
    return redirect('pagina-programacao')


