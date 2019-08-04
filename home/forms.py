from django import forms
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'What should I call you ? '}))
    email = forms.EmailField(label='Your Email ID', widget=forms.TextInput(attrs={'placeholder': 'Where can I email you back ?'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'What\'s on your mind ?'}) )

class CommentForm(forms.ModelForm):

    class Meta :
        model = Comment
        fields = "__all__"


