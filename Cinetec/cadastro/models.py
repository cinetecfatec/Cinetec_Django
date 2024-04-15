from django.db import models
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class NovoCadastro(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(NovoCadastro, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'CriarCadastro'))
        self.helper.template = 'bootstrap5' 