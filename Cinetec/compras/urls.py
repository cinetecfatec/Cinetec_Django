from django.urls import path
from . import views
from .views import finalizar_compra

urlpatterns = [
    path("programacao/<str:data_esc>/", views.ProgramacaoListView.as_view(), name="pagina-programacao"),
    path("data_escolhida/", views.DataEscolhidaView.as_view(), name="data_escolhida"),
    path("compra/<int:pk>/", views.CompraListView.as_view(), name="pagina-compra"),
    path("ingresso_escolhido/", views.IngressoEscolhidoView.as_view(), name="ingresso-escolhido"),
    path("checkout/", views.CheckoutListview.as_view(), name="pagina-checkout"),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
]
