from django.contrib import admin
from django.urls import path, include
from .views import CadastroCreateView,CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro_novo/', CadastroCreateView.as_view(), name='pagina-cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='pagina-login'),
    path('logout/', CustomLogoutView.as_view(), name='pagina-logout'),
]
