from django.contrib import admin
from django.urls import path,include
from .views import CustomLoginView, cadastroCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cadastro_novo/", cadastroCreateView.as_view(), name="pagina-cadastro"),
    path('login/', CustomLoginView.as_view(), name='pagina-login'),
    path("logout/", auth_views.LoginView.as_view(template_name = 'logout.html'), name="pagina-logout"),
]

