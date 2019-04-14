from django.views.generic import ListView

from .models import MyTodo


class Index(ListView):
    model = MyTodo
    context_object_name = "lst_my_works"
    template_name = "base.html"
