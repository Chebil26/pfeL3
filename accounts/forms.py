from django import forms
#rom django.db.models import fields


from .models import *


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user' , 'abonnement']
        widgets = {'date_de_naissaince': forms.DateInput(attrs={'type':'date'})}



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'date_joined']



    

    # class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


# class choisir_abonnement(ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['abonnmentChoisit']
#         exclude = ['user']

    #     # abonnmentChoisit = forms.ModelMultipleChoiceField(
    #     # queryset=Abonnement.objects.all(),
    #     # widget=forms.CheckboxSelectMultiple
    # )


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']



class AbonnementModelForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = '__all__'
        exclude = ['coach']
        
        widgets = {'date': forms.DateInput(attrs={'type':'date'})}



class AvisModelForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = '__all__'
        exclude = ['auteur']


# class AjouterAbonnement(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['abonnmentChoisit' , 'name']




class OrderFormAB(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['abonne', 'seance']


class OrderFormSE(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['abonne' , 'abonnement']