from django.urls import path,include
from .views import IngressoTemplateview

urlpatterns = [
    path("compras/ingresso", IngressoTemplateview.as_view(), name="pagina-ingresso"),
]