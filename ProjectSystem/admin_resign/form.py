from django import forms

class resign_form(forms.Form):
    username = forms.CharField(max_length=30)
    sex = forms.CharField(max_length=30)
    birthday = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    mobile = forms.CharField(max_length=30)
    cardname = forms.CharField(max_length=30)
    level = forms.CharField(max_length=30)
