from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User  # Import User model
from django.urls import reverse_lazy
from .models import NovoCadastro,LoginForm
from  django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.

class cadastroCreateView(CreateView):
    model = User
    form_class = NovoCadastro
    template_name = "cadastroNovo.html"
    success_url = reverse_lazy('pagina-inicio')
    
    def form_valid(self, form):
        # Custom logic before saving the form
        # For example, you might modify form data or perform additional validation
        
        # Call the parent class's form_valid method to save the form
        response = super().form_valid(form)
        
        # Custom logic after saving the form
        # For example, you might send a notification email or log the form submission
        
        return response

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm  # Assuming you have a custom login form

