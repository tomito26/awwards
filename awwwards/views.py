from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Project
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name='awwwards/home.html'
    context_object_name= 'projects'
    ordering = ['-date_posted']


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'awwwards/project_detail.html'

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = [
        'title', 'description', 'project_image', 'link', 'country'
    ]
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'project_image', 'link', 'country']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project= self.get_object()
        if self.request.user == project.author:
            return True
        
        return False

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Project
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        
        return False