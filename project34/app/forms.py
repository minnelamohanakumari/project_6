from django import forms
class StudentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField()
    email=forms.EmailField()