from django import forms

from .models import Tweet

MAX_TWEET_LENGTH = 240
class TweetForm(forms.ModelForm):
    class Meta: 
        model = Tweet
        fields = ['contant']

    def clean_content(self):
        content = self.cleaned_data("contant")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content