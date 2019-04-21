from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_todo, name='add_todo'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_todo, name='delete_todo'),

]
