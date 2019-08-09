from django import forms
from .models import Comment, Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(label='Your Email ID', widget=forms.TextInput(attrs={'placeholder': 'Where can I email you back ?'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'What\'s on your mind ?'}))

    class Meta:
        model = Contact
        fields = "__all__"

class CommentForm(forms.ModelForm):

    sender = forms.CharField(max_length=100, label='Your Name',
                           widget=forms.TextInput(attrs={'placeholder': 'What\'s  your name ?'}))

    class Meta:
        model = Comment
        fields = "__all__"

        widgets = {
            'caption': forms.Textarea(attrs={'placeholder': 'What\'s on your mind ?'})
        }

