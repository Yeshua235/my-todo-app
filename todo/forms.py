
from django import forms
from .models import Todo

class DoneForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'title',
            'body',
            'time_to_start',
            'time_to_finish',
            'done',
        )
        widgets = {
            'time_to_start':forms.DateTimeInput(attrs={'type':'datetime-local'}),  # this is the same as 'time_to_start':forms.DateTimeInput(format='%Y-%m-%dT%H:%M'), but the latter is more explicit.
            'time_to_finish':forms.DateTimeInput(attrs={'type':'datetime-local'}), # this is the same as 'time_to_finish':forms.DateTimeInput(format='%Y-%m-%dT%H:%M'), but the latter is more explicit.
            'body':forms.Textarea,
            'done':forms.CheckboxInput,
            }
        #Done = forms.BooleanField(widget=forms.CheckboxInput)     # both this and the one above does the same thing. 
