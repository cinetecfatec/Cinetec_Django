from django.urls import path,include
from .views import IngressoTemplateview,ProgramacaoListView,DataEscolhidaView,CompraListView,IngressoEscolhidoView,CheckoutListview

urlpatterns = [
    path("compras/ingresso", IngressoTemplateview.as_view(), name="pagina-ingresso"),
    path("programacao/<str:data_esc>/", ProgramacaoListView.as_view(), name="pagina-programacao"),
    path("data_escolhida/", DataEscolhidaView.as_view(), name="data_escolhida"),
    path("compra/<int:pk>/", CompraListView.as_view(), name="pagina-compra"),
    path("ingresso_escolhido/", IngressoEscolhidoView.as_view(), name="ingresso_escolhido"),
    path("checkout/<str:assentos_check>/", CheckoutListview.as_view(), name="Pagina-checkout"),
]