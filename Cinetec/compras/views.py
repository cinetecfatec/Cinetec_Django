from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from filmes.models import listaFilmes
from .models import Sessoes
from datetime import date
from django.shortcuts import redirect
from django.urls import reverse
from .forms import MeuForm
from django.http import HttpResponse

class IngressoTemplateview(TemplateView):
    template_name = "pagina-compras"

class ProgramacaoListView(ListView):
    template_name = "programacao.html"
    context_object_name = 'dados'

    def get_queryset(self):
        filmes = listaFilmes.objects.all()
        sessoes = Sessoes.objects.all()
        datas = Sessoes.objects.filter(data_sessao__gte=date.today()).values('data_sessao').distinct().order_by('data_sessao')
        hoje = date.today()
        return {'filmes': filmes, 'sessoes': sessoes, 'datas': datas, 'hoje': hoje}


class DataEscolhidaView(TemplateView):
    template_name = "data_escolhida"
    form_class = MeuForm
    success_url = 'pagina-programacao'

    def form_valid(self):
        if request.method == 'POST':
            valor_selecionado = request.POST.get('opcao')
            # Faça o processamento necessário com o valor selecionado
            # Aqui você pode retornar qualquer resposta que desejar
            return HttpResponse("Valor selecionado: " + valor_selecionado)
        else:
            return HttpResponse("Método não permitido")
        
    # e no fim retorna o form para que o submit ocorra.
        #return super().form_valid(form)

class CompraDetailView(DetailView):
    model = listaFilmes    
    template_name = "Compra.html"