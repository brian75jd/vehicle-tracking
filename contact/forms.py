from .models import SendMessage
from django import forms

class SendUsMessage(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Write your message.....',
        'class':'',
        'required':True,
    }))
    class Meta:
        model = SendMessage
        fields = ['content']
