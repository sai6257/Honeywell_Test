from django import forms

class CDRFileUploadForm(forms.Form):
    cdr_file = forms.FileField()
