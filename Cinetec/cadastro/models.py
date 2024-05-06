from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User

class NovoCadastro(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
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
        self.helper.form_method = 'POST'
        self.helper.form_class = 'cadastroForm'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
        self.helper.label_class = 'col-md-3 col-form-label'
