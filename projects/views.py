from django.shortcuts import render, redirect
from .models import Projects, Tasks
from .forms import ProjectsForm, TasksForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.


def projects_home(request):
    projects = Projects.objects.prefetch_related('task').order_by('id')
    #  project = Projects.objects.prefetch_related('tasks').all()
    return render(request, 'projects/projects_home.html', {'projects': projects})


class ProjectsDetailView(DetailView):
    model = Projects
    template_name = 'projects/details_view.html'
    context_object_name = 'project'


class ProjectsUpdateView(UpdateView):
    model = Projects
    template_name = 'projects/project-update.html'
    form_class = ProjectsForm


class ProjectsDeleteView(DeleteView):
    model = Projects
    template_name = 'projects/project-delete.html'
    success_url = '/projects'


class TasksUpdateView(UpdateView):
    model = Tasks
    template_name = 'projects/task-update.html'
    form_class = TasksForm


class TasksDeleteView(DeleteView):
    model = Tasks
    template_name = 'projects/task-delete.html'
    success_url = '/projects'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_home')
        else:
            error = 'Форма была неверной'

    form = ProjectsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'projects/create.html', data)


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_home')
        else:
            error = 'Форма была неверной'

    form = TasksForm()

    data = {
        'form_task': form,
        'error_task': error
    }

    return render(request, 'projects/create_task.html', data)
