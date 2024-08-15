from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from webapp.models import Record

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


#create
class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Record

        fields = '__all__'



#update
class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = Record

        fields = '__all__'