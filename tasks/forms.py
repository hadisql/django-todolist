from django import forms

from .models import Task

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority',)

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Title e.g "Shopping with Emma"'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Task description'
    }), required=False)

    priority = forms.NumberInput(attrs={'class': 'py-4 rounded-md'})


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority',)

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Title e.g "Shopping with Emma"'
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Task description'
    }))

    priority = forms.NumberInput(attrs={'class': 'py-4 rounded-md'})
