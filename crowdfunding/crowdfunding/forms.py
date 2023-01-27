from django import forms
from .models import Comment


class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
