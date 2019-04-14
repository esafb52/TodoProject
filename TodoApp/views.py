from django.http import HttpResponse


def index(request):
    return HttpResponse("hello word! this is todo app")
