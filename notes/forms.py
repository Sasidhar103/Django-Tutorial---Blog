from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(max_length=25)
    content = forms.CharField(max_length=250)
    image = forms.FileField()
