from django.db import models
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(blank=False, null=False)    
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='cadastro_users')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='cadastro_users',
        help_text=_('Specific permissions for this user.'),
    )

class NovoCadastro(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'required': True}),
        }
        labels = {
            'username': 'Nome de Usuário',  # Altera o rótulo do campo username
            'email' : 'E-mail',
        }
        help_texts = {
            'username': None,  # Removendo o texto de ajuda do campo password
        }
    
    def __init__(self, *args, **kwargs):
        super(NovoCadastro, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'cadastroForm'
        self.helper.add_input(Submit('submit', 'Criar Cadastro', css_class='btn btn-primary'))  
        
