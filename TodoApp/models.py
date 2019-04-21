from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels


class MyTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.CharField(max_length=350)
    state_complete = models.BooleanField(default=False)


    def __str__(self):
        return self.work
