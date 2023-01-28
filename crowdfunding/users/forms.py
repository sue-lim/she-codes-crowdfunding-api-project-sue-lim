from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',  'email',
                  'bio', 'profile_picture', 'linkedin', 'instagram']

        widgets = {
            'username': forms.TextInput({'size': '45', 'size': '45', 'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput({'size': '45', 'size': '45', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput({'size': '45', 'size': '45', 'placeholder': 'Enter your last name'}),
            # 'bio': forms.Textarea({'placeholder': 'Tell us more about yourself......'}),
            'profile_picture': forms.URLInput({'size': '45', 'placeholder': 'https://...'}),
            'email': forms.TextInput({'size': '45', 'size': '45', 'placeholder': 'Enter your email'}),
            # 'linkedin': forms.TextInput({'size': '45', 'size': '45', 'placeholder': 'https://www.linkedin.com/in/'}),
            # 'instagram': forms.TextInput({'size': '45', 'size': '45', 'placeholder': ''}),
            'password': forms.TextInput(attrs={'type': 'password'})
        }
