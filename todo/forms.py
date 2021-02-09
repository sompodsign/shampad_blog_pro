from django.forms import ModelForm
from todo.models import TODO
from django import forms


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
    }
