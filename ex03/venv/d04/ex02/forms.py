from django import forms

class MyForm(forms.Form):
    your_text = forms.CharField(label='Your text here ')
