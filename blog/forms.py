from dataclasses import field
from django import forms
from django.forms import ModelForm, Textarea
from blog.models import Comment, Blog

# Create your forms here.

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'body': Textarea(attrs={'cols': 30, 'rows': 5}),
        }

        fields = '__all__'
        exclude = ['user_pic','user_address','blog','commented_on']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.help_text