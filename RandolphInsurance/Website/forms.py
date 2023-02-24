# forms.py
from django import forms
from .validators import validate_file_size

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, validators=[validate_file_size])
    message = forms.CharField(widget = forms.Textarea)