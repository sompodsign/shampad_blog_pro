from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'review',
                  'rating', 'img_url',
                  'watch', 'type',
                  'active')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control',
                                              'style': 'margin-bottom: 10px;'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'img_url', 'watch', 'active')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control',
                                              'style': 'margin-bottom: 10px;'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
        }
