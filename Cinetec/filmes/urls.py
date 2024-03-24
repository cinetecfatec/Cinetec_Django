from django.urls import path
from .views import indexView,sobreView

urlpatterns = [
    path("inicio/", indexView.as_view(), name="inicio"),
    path("sobre_nos/", sobreView.as_view(), name="sobre")
]

