from django.urls import path
from .views import indexListView,sobreView,escolhidoDetailView,programacaoListView

urlpatterns = [
    path("cinetec/", indexListView.as_view(), name="pagina-inicio"),
    path("sobre_nos/", sobreView.as_view(), name="pagina-sobre"),
    path("escolhido/<int:pk>/", escolhidoDetailView.as_view(), name="pagina-escolhido"),
    path("programacao/", programacaoListView.as_view(), name="pagina-programacao")
]

