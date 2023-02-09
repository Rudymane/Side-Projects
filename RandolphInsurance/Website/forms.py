# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    message = forms.CharField(widget = forms.Textarea)