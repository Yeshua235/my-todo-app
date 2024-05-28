from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Todo
from django.urls import reverse_lazy, reverse
from .forms import DoneForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from pytz import UTC

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.completed_at != None:
            delta = self.object.completed_at - self.object.time_to_start
            years = delta.days//365
            months = (delta.days % 365) // 30
            days = (delta.days % 365) % 30
            hours = delta.seconds // 3600
            mins = (delta.seconds // 60) % 60
            secs = delta.seconds % 60
            duration = f'{years} yrs, {months} months, {days} days, {hours} hours, {mins} minutes and {secs} seconds.'
            context['time_taken'] = duration
            return context
        else:
            return context


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    form_class = DoneForm
    template_name = 'todo_edit.html'

    
    def form_valid(self, form):
        completed_tasks = form.cleaned_data['done']
        if form.cleaned_data['done']:
            self.object.completed_at = datetime.now()
        return super().form_valid(form)
    
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    
    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.get_object().pk,})

#class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
#    def post(self, request, id, *args, **kwargs):
#        todo = Todo.objects.get(id=id)
#        done = request.POST.get('is_completed')
#        if done:
#            todo.done = True
#            todo.completed_at = datetime.now()
#        return reverse('todo_detail',kwargs={'pk': self.get_object().pk,})
    

#    def get_object(self):
#        return Todo.objects.get(pk=self.kwargs['pk'])
    
#    def test_func(self):
#        obj = self.get_object()
#        return obj.author == self.request.user
    
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
        completed_tasks = form.cleaned_data['done']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo_list')
