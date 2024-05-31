from django import forms



class customer_form(forms.Form):
    first_name =forms.CharField()
    last_name =forms.CharField()
    email =forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

