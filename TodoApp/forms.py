from django import forms

from TodoApp.models import MyTodo


class AddTodoForm(forms.Form):
    work_txt = forms.CharField(max_length=300, help_text='متن کار خود را جهت ثبت وارد نمایید',
                               error_messages={'required': 'Please choose a star rating'},

                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'کار خود را وارد نمایید',

                                          'aria-label': 'Todo',
                                          'aria-describedby': 'add-btn'}))


class TodoForm(forms.ModelForm):
    class Meta:
        model = MyTodo
        fields = ('work', 'state_complete')
