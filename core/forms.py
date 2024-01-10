from django import forms
from core.models import UserModel, CommentModel
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'placeholder': 'Username*',
                    'type': 'text',
                    'class': 'form-control',
                    'name': 'username'
                }
            ),
            'surname': forms.TextInput(
                attrs = {
                    'placeholder': 'Surname*',
                    'type': 'text',
                    'class': 'form-control',
                    'name': 'surname'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'Email*',
                    'type': 'email',
                    'class': 'form-control',
                    'name': 'email'
                }
            ),
        }
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            if len(password) == 0:
                raise ValidationError('This field is required.')
            else:
                raise ValidationError('Your password must be at least 8 characters.')
        
        else: return password
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {
            'placeholder': 'Password*',
            'class': 'form-control',
            'type': 'password'
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': 'Password Confirm*',
            'class': 'form-control',
            'type': 'password'
        }

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=30, widget = forms.TextInput(attrs = {'name': 'username', 'placeholder': 'Username', 'type': 'text', 'class': 'form-control mt-5 p-3'}))
    password = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {'name': 'password', 'placeholder': 'Password', 'type': 'password', 'class': 'form-control mt-5 p-3'}))

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(
                attrs= {
                    'placeholder': 'Write your comment',
                    'type': 'text',
                    'class': 'form-control'
                }
            )
        }
