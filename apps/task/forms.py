from django import forms

from . import models

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'skill', 'duration', 'deadline' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'rows':'2'}),
            'duration' : forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':'Duration'}),
            'skill' : forms.Select(attrs={'class': 'form-control'}),
            'deadline' : forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'placeholder':'YYYY-MM-DD'}),
        }

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'start_date', 'end_date' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
            'start_date' : forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'placeholder':'YYYY-MM-DD'}),
            'end_date' : forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'placeholder':'YYYY-MM-DD'}),
        }
