from django.urls import path,include
from .views import IngressoTemplateview,ProgramacaoListView

urlpatterns = [
    path("compras/ingresso", IngressoTemplateview.as_view(), name="pagina-ingresso"),
    path("programacao/", ProgramacaoListView.as_view(), name="pagina-programacao")
]