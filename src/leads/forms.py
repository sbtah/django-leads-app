from django import forms
from django.forms import ModelForm
from .models import Lead


class LeadModelForm(ModelForm):
    class Meta:

        model = Lead

        fields = ('first_name', 'last_name', 'age', 'agent')

        # widgets = {
        #     'first_name': forms.TextInput(),
        #     'last_name': forms.TextInput(),
        #     'age': forms.IntegerField(min_value=0),
        #     'agent': forms.Select(),
        # }


# class LeadForm(forms.Form):

#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=0)
