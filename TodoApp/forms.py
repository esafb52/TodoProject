from django import forms

from TodoApp.models import MyTodo


class AddTodoForm(forms.Form):
    work_txt = forms.CharField(max_length=300,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'کار خود را وارد نمایید',
                                          'aria-label': 'Todo',
                                          'aria-describedby': 'add-btn'}))


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['work'].widget.attrs.update({
            'placeholder': 'کار خود را وارد نمایید',


        })

    class Meta:
        model = MyTodo
        fields = ('work',)
