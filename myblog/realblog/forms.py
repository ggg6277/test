from django import forms
import datetime
from .models import Contents, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('author','body')
