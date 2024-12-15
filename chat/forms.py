# from django.forms import ModelForm
# from django import forms
# from .models import *

# class ChatMessageCreateForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['content']
#         widgets = {
#             'content' : forms.TextInput(attrs={'placeholder':'Add message...',
#                                                'class':'p-4 text-black',
#                                                 'maxlength':'300',
#                                                 'autofocus':True }),
#         }

from django import forms
from .models import Message

class ChatMessageCreateForm(forms.Form):
    content = forms.CharField(max_length=300)
    author = forms.CharField()
    chatroom = forms.CharField()  # ReferenceField will need to be handled manually if you require ID or object here

    def save(self, commit=True):
        # Create a new `Message` instance using form data
        message = Message(
            content=self.cleaned_data['content'],
            author=self.cleaned_data['author'],
            chatroom=self.cleaned_data['chatroom'] 
        )
        if commit:
            message.save()
        return message
