from django import forms
from .models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'surname', 'middle_name', 'about']
