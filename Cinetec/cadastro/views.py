from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import NovoCadastro, LoginForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect


class CadastroCreateView(CreateView):
    model = User
    form_class = NovoCadastro
    template_name = "cadastroNovo.html"
    success_url = reverse_lazy('pagina-inicio')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.is_staff = True
        self.object.save()
        return response

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy('pagina-inicio')

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('pagina-login')


