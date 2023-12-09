from django import forms
from .models import ContactMessage, Post

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'description']