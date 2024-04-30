from django import forms
from App.models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="TEXT EDITOR")
    class Meta:
        model = Post
        fields = ('body',)