from django.shortcuts import render, redirect
from .forms import TODOForm
from .models import TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def todo_list(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'todo/todo.html', {'form': form, 'todos': todos})


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('todo:todos')
        else:
            return render(request, 'todo/todo.html', context={'form': form})


def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('todo:todos')


def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('todo:todos')
