from django import forms

from datetime import  date

from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('__all__')
        labels = {
            'done': 'Is this task done?'
        }
        help_texts = {
            'due_date': 'Date when the task is expected to be done'
        }


    def clean_title(self):
        title = self.cleaned_data['title']

        words = title.split(' ')
        if len(words) > 5:
            raise forms.ValidationError('The title should be five or less words.')
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']

        if due_date < date.today():
            raise forms.ValidationError('The due date cannot be in the past.')
        return due_date
    
