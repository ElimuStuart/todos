from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime
from django.views.generic import (
    CreateView, UpdateView, ListView, DetailView, View, DeleteView
)
from django.urls import reverse_lazy

from . models import Todo
from . forms import TodoForm



class IndexView(ListView):
    queryset = Todo.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['today'] = datetime.now().date()
        ctx['app_name'] = 'Super Todos'
        return ctx


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'today': datetime.now(),
        'app_name': 'Super todos',
    }
    
    return render(request, 'main/index.html', context=context)



class TodoDetailView(DetailView):

    model = Todo

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    context = {
        'todo': todo,
    }
    return render(request, 'main/todo_detail.html', context=context)


class TodoCreateView(SuccessMessageMixin, CreateView):

    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been created successfully.'


class TodoUpdateView(SuccessMessageMixin, UpdateView):

    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been updated successfully.'

# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'The todo was created successfully.')
#             return redirect('index')
#         else:
#             return render(request, 'main/todo.html', {'form': form})
#     else:
#         return render(request, 'main/todo.html', {'form': TodoForm()})


def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'The todo was updated successfully.')
            return redirect('index')
        else:
            return render(request, 'main/todo.html', {'form': form})
    else:
        return render(request, 'main/todo.html', {'form': TodoForm(instance=todo)})


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'main/todo_delete.html'
    success_url = reverse_lazy('index')
    success_message = 'The todo was deleted successfully.'



def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'The todo was deleted successfully.')
        return redirect('index')
    return render(request, 'main/todo_delete.html', {'todo': todo})
    

class TodoJsonView(View):

    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(done=True).values()
        return JsonResponse({'todos': list(todos)})

