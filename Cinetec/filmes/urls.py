from django.urls import path
from .views import indexView,sobreView

urlpatterns = [
    path("cinetec/", indexView.as_view(), name="pagina-inicio"),
    path("sobre_nos/", sobreView.as_view(), name="pagina-sobre")
]

