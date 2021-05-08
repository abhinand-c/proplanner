from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from . import models, forms

# Create your views here.

class TaskView(TemplateView):
    """ Page showing list of tasks & actions for all Employee """
    template_name = "task/home.html"    # To do - Employee Task Page

    def get_context_data(self, *args, **kwargs):
        context = super(TaskView, self).get_context_data(*args, **kwargs)
        return context


class ManagerDash(TemplateView):
    template_name = "task/manager_dash.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ManagerDash, self).get_context_data(*args, **kwargs)
        context['project_list'] = self.get_project_list()
        return context

    def get_project_list(self):
        return models.Project.objects.filter()

class ManagerProjectDetail(TemplateView):
    template_name = "task/manager_prodetail.html"
    create_task_form = forms.CreateTaskForm()
    def get_context_data(self, *args, **kwargs):
        context = super(ManagerProjectDetail, self).get_context_data(*args, **kwargs)
        context['task_list'] = self.get_task_list()
        print(dir(self.get_task_list()))
        context['create_task_form'] = self.create_task_form
        return context

    def get_project(self):
        return models.Project.objects.get(pk=self.kwargs['pk'])

    def get_task_list(self):
        return models.Task.objects.filter(project=self.get_project())


    def post(self, request, *args, **kwargs):
        if 'create-task' in request.POST :
            form = forms.CreateTaskForm(request.POST)
            if form.is_valid():
                return self.CreateTask_valid(form)
            self.create_task_form = form
        return self.get(request, *args, **kwargs)

    def CreateTask_valid(self, form):
        task_model = form.save(commit=False)
        task_model.project = self.get_project()
        task_model.created_by = self.request.user
        task_model.save()
        messages.success(request, 'Task Added!')
        return self.get(request, *args, **kwargs)
