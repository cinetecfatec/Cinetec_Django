from django.urls import path,include
from .views import IngressoTemplateview,ProgramacaoListView,DataEscolhidaView,CompraDetailView

urlpatterns = [
    path("compras/ingresso", IngressoTemplateview.as_view(), name="pagina-ingresso"),
    path("programacao/", ProgramacaoListView.as_view(), name="pagina-programacao"),
    path("data_escolhida/", DataEscolhidaView.as_view(), name="data_escolhida"),
    path("compra/<int:pk>/", CompraDetailView.as_view(), name="pagina-compra"),
]