from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import AdminProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class AdminProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AdminProfile
        widgets = {
        'password': forms.PasswordInput(),
     }
        labels = {
            "adminname": "Admin Name",
            "password": "Password",
            "institutiontype": "Institution Type",
            "institutionname": "Institution Name",
            "testallowed": "Test Allowed",
            "noofuser": "No of User's",
            
        }
        fields = "__all__"    

