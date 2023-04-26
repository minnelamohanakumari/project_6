from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','url']
        #exclude=['name']
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea}
        #labels={'topic_name':'TN','name':'N'}
        help_text={'topic_name':'sholud not be integers','name':'only alphabets'}
class AccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
        #fields=['name','date']
        #exclude=['author']
        widgets={'name':forms.PasswordInput,'author':forms.Textarea(attrs={'cols':3,'rows':3})}
        #labels={'name':'N','author':'A'}
        #help_text={'name':'only alphabets can allow'}