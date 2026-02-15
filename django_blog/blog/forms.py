from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
