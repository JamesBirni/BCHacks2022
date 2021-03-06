from django import forms
from Profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'bio', 'location', 'birth_date']
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'email']

