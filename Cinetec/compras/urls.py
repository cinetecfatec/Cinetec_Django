from django.urls import path
from . import views

urlpatterns = [
    path("compras/ingresso", views.IngressoTemplateview.as_view(), name="pagina-ingresso"),
    path("programacao/<str:data_esc>/", views.ProgramacaoListView.as_view(), name="pagina-programacao"),
    path("data_escolhida/", views.DataEscolhidaView.as_view(), name="data_escolhida"),
    path("compra/<int:pk>/", views.CompraListView.as_view(), name="pagina-compra"),
    path("compras/ingresso_escolhido/", views.IngressoEscolhidoView.as_view(), name="ingresso-escolhido"),
    path("checkout/<str:assentos_check>/", views.CheckoutListview.as_view(), name="Pagina-checkout"),
]