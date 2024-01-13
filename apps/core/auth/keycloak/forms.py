from django.forms import forms


class AuthenticationForm(forms.Form):
    auth_token = forms.CharField()
