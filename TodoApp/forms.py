from django import forms


class AddTodoForm(forms.Form):

    work_txt = forms.CharField(max_length=300,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'کار خود را وارد نمایید',
                                          'aria-label': 'Todo',
                                          'aria-describedby': 'add-btn'}))
