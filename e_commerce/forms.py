from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite nome completo..."
                }
            )
        )
    email     = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email..."
                }
            )
        )
    texto   = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem.."
                }
            )
        )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email

class LoginForm(forms.Form):
    usuário = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu usuário..."
                }
            )
    )
    senha = forms.CharField(widget=forms.PasswordInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua senha..."
                }
            )
    )

class RegisterForm(forms.Form):
    usuário = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite o seu usuário..."
                }
            )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu e-mail..."
                }
            )
    )
    senha = forms.CharField(widget=forms.PasswordInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua senha..."
                }
            )
    )
    senha2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Repita sua senha..."
                }
            )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data