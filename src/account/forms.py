from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class SignupForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Password Repeat", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password_repeat"]:
            raise forms.ValidationError("Password do not match")

        return cd["password_repeat"]
