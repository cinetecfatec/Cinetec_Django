from django import forms
from datetime import date

class MeuForm(forms.Form):
    data_esc = forms.DateField(initial=date.today(), required=False)