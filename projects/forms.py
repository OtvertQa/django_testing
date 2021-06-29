from .models import Projects, Tasks
from django.forms import ModelForm, TextInput, DateInput, Select, Textarea


PROJECT_STATUS = (
            ('Not started', 'Not started'),
            ('Active', 'Active'),
            ('Completed', 'Completed'),
        )

TASK_STATUS = (
        ('To Do', 'To Do'),
        ('In progress', 'In Progress'),
        ('Done', 'Done'),
    )


class ProjectsForm(ModelForm):

    class Meta:
        model = Projects
        fields = ['title', 'start_date', 'finish_date', 'status']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project name'
            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project start date'
            }),
            "finish_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project end date'
            }),
            "status":  Select(attrs={
                'class': 'form-control',
                'placeholder': 'Project status',
                'choices': PROJECT_STATUS
            })

        }


class TasksForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['project', 'name', 'status', 'description']

        widgets = {
            "project": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Project name',
                'choices': Projects.objects.all()
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task name'
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Task status',
                'choices': TASK_STATUS
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Task description'
            })

        }
