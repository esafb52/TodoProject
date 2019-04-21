from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddTodoForm
from .models import MyTodo


def index(request):
    todo_list = MyTodo.objects.order_by('id')
    form = AddTodoForm()
    context = {'lst_my_works': todo_list, 'form': form}
    return render(request, 'content.html', context)


def add_todo(request):
    user = User.objects.all()
    work = request.POST['work_txt']
    todo = MyTodo(work=work, user=user[0], state_complete=False)
    todo.save()
    return redirect('index')


def delete_todo(request, id):
    get_object_or_404(MyTodo, pk=id).delete()
    return redirect('index')


def complete_todo(request, id):
    this_todo = MyTodo.objects.get(pk=id)
    this_todo.state_complete = True
    this_todo.save()
    return redirect('index')


def incomplete_todo(request, id):
    this_todo = MyTodo.objects.get(pk=id)
    this_todo.state_complete = False
    this_todo.save()
    return redirect('index')
