from django import forms

from .models import Task, Tag

class NewTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority','tags')

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Title e.g "Shopping with Emma"'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Task description'
    }), required=False)

    #priority = forms.NumberInput(attrs={'class': 'py-4 rounded-md'})
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, widget=forms.RadioSelect())

    #tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
    #                                      queryset=Tag.objects.all())


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
    }), required=False)

    #priority = forms.NumberInput(attrs={'class': 'py-4 rounded-md'})
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, widget=forms.RadioSelect())

    #tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
    #                                      queryset=Tag.objects.all())
