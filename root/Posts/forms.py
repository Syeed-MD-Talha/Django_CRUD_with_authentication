from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','id':'postTitle', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control','id':'postContent', 'placeholder': 'Content'}),
            'author': forms.TextInput(attrs={'class': 'form-control','id':'postAuthor', 'placeholder': 'Author'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
