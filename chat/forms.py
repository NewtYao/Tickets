from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content' : forms.TextInput(attrs={'placeholder':'Add message...',
                                               'class':'p-4 text-black',
                                                'maxlength':'300',
                                                'autofocus':True }),
        }