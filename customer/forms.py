from django import forms
from django.core import validators



class customer_form(forms.Form):
    first_name =forms.CharField()
    last_name =forms.CharField()
    email =forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data= super().clean()
        rpassword=self.cleaned_data['password']
        wpassword=self.cleaned_data['repassword']
        if rpassword!=wpassword:
            raise forms.ValidationError("Passwords don't match")


