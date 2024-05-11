from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from filmes.models import listaFilmes
from .models import Sessoes
from datetime import date
from django.http import JsonResponse

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
        return {'filmes': filmes, 'sessoes': sessoes, 'datas': datas, 'hoje': hoje}

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data_esc = request.POST.get('valor')
            # Aqui você pode processar o valor conforme necessário
            # Por exemplo, você pode retornar uma resposta JSON com os resultados do processamento
            return JsonResponse({'status': 'success', 'valor': data_esc})
        else:
            return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido'}, status=400)
