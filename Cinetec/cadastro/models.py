from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class NovoCadastro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
        }
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
        }
        help_texts = {
            'username': None,
            'password1': None,

        }

    def __init__(self, *args, **kwargs):
        super(NovoCadastro, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'cadastroForm'
        self.helper.add_input(Submit('submit', 'Registrar', css_class='btn btn-primary'))
        self.helper.label_class = 'col-md-3 col-form-label'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'loginForm'
        self.helper.add_input(Submit('submit', 'Login', css_class='btn btn-primary'))
        self.helper.label_class = 'col-md-3 col-form-label'
