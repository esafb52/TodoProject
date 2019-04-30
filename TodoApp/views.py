from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddTodoForm, TodoForm
from .models import MyTodo


def index(request):
    todo_list = MyTodo.objects.order_by('state_complete')
    form = AddTodoForm()
    context = {'lst_my_works': todo_list, 'form': form}
    return render(request, 'content.html', context)


def add_todo(request):
    user = User.objects.all()
    work = request.POST['work_txt']
    todo = MyTodo(work=work, user=user[0], state_complete=False)
    todo.save()
    return redirect('index')


def delete_todo(request, todo_id):
    get_object_or_404(MyTodo, pk=todo_id).delete()
    messages.add_message(request, messages.INFO, 'سطر مد نظر حذف شد ')
    return redirect('index')


def edit_todo(request, todo_id):
    if request.method == 'POST':
        item = MyTodo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
        print(form.errors)
    else:
        print('get run ')
        item = MyTodo.objects.get(pk=todo_id)
        return render(request, 'edit_todo.html', {'item': item})


def complete_todo(request, todo_id):
    this_todo = MyTodo.objects.get(pk=todo_id)
    this_todo.state_complete = True
    this_todo.save()
    return redirect('index')


def incomplete_todo(request, todo_id):
    this_todo = MyTodo.objects.get(pk=todo_id)
    this_todo.state_complete = False
    this_todo.save()
    return redirect('index')


def about(request):
    context = {}
    return render(request, 'about.html', context)
