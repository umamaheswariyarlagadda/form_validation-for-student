from django import forms
from django.forms import ModelForm
from.models import Post
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=["username","gender","text"]

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        text=cleaned_data.get('text')
        if username and len(username)<5:
            self.add_error('username','Minimum 5 characters required.')
        if text and len(text)<10:
            self.add_error('text','Post should contain atleast 10 characters.')
        return cleaned_data
