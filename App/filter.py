import django_filters
from django import forms
from django_filters import CharFilter

from App.models import Trainer


class TrainerNameFilter(django_filters.FilterSet):
    type = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search with Trainer type','class':'form-control me-3 ','style':'width:30rem'
    }))
    class Meta:
        model = Trainer
        fields = ('type',)