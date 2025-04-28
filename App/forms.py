from django import forms
from django.contrib.auth.forms import UserCreationForm

from App.models import LoginView, Trainer, Member, WorkOutPlan, Community


class LoginUserForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder':'Enter Your User Name '
    }))
    password1 = forms.CharField(label ='',widget =forms.PasswordInput(attrs={
        'placeholder':'Create a Password'
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder':'Re-enter Your Password '
    }))

    class Meta:
        model = LoginView
        fields = ('username','password1','password2')


class TrainerForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Name '
    }))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Email '
    }))
    phoneNo = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Phone No '
    }))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Address '
    }))
    proof = forms.FileField(label='')
    type =forms.ChoiceField(label='',choices=Trainer._meta.get_field('type').choices)

    class Meta:
        model = Trainer
        fields = ('name', 'email', 'phoneNo', 'address', 'proof','type')


class MemberForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Name '
    }))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Email '
    }))
    phoneNo = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Phone No '
    }))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Address '
    }))


    class Meta:
        model = Member
        fields = ('name', 'email', 'phoneNo', 'address')



class WorkOutPlanForm(forms.ModelForm):
    type = forms.ChoiceField(label='',choices=WorkOutPlan._meta.get_field('type').choices)
    plan = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','rows':'8','cols':'30'}))

    class Meta:
        model = WorkOutPlan
        fields = ('type','plan')


class CommunityForm(forms.ModelForm):
    msg = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Message', 'class': 'form-control', 'style': 'width:30rem;'
    }))
    picture = forms.ImageField(label='',required=False)
    class Meta:
        model = Community
        fields = ('msg','picture')
