from django import forms
from django.forms import ModelForm
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


User = get_user_model()


class LeadForm(ModelForm):

    class Meta:

        model = Lead

        fields = ('__all__')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'agent': 'Agent',
        }


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:

        model = User
        fields = ('username', 'password1', 'password2',)
        field_classes = {'username': UsernameField}
