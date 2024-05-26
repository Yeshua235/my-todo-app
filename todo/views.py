from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Todo
from django.urls import reverse_lazy, reverse
from .forms import DoneForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list']= self.object_list
        context['todo_list_indices'] = range(1, len(self.object_list)+1)
        return context
    
    def get_queryset(self):
        return Todo.objects.filter(author = self.request.user)

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo_detail.html'


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    form_class = DoneForm
    template_name = 'todo_edit.html'
    #success_url = 
    
    def form_valid(self, form):
        completed_tasks = form.cleaned_data['Done']
        return super().form_valid(form)
    
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    
    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.get_object().pk,})

    
class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
    
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = DoneForm
    template_name = "todo_new.html"
#    fields = (                 #can't use fields and form_class together
#        "title",
#        "body",
#        "author",
#    )
#    success_url = reverse_lazy('todo_detail', kwargs={'pk':Todo.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        completed_tasks = form.cleaned_data['Done']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo_list')
