from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    leadername = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email1 = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    contact1 = forms.IntegerField()
    branch1 = forms.CharField(max_length=100)

    participant2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email2 = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    contact2 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    branch2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


    participant3 =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email3 = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    contact3 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    branch3 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username


    def clean(self):
        data =self.cleaned_data
        password1=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if password2!=password1:
            raise forms.ValidationError("Password must be same")
        return data


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))