
from django import forms
from .models import Todo

class DoneForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'title',
            'body',
            'Done',
        )
        widgets = {
            'Done':forms.CheckboxInput,
            }
        #Done = forms.BooleanField(widget=forms.CheckboxInput)     # both this and the one above does the same thing. 
