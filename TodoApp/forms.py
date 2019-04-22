from django import forms

from TodoApp.models import MyTodo


class AddTodoForm(forms.Form):
    work_txt = forms.CharField(max_length=300,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'کار خود را وارد نمایید',
                                          'aria-label': 'Todo',
                                          'aria-describedby': 'add-btn'}))


class TodoForm(forms.ModelForm):
    class Meta:
        model = MyTodo
        fields = ('work',)
