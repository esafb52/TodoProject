from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_todo, name='add_todo'),
    url(r'^about$', views.about, name='about'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_todo, name='delete_todo'),
    url(r'^complete/(?P<id>\d+)/$', views.complete_todo, name='complete_todo'),
    url(r'^incomplete/(?P<id>\d+)/$', views.incomplete_todo, name='incomplete_todo'),
    url(r'^edit_todo/(?P<todo_id>\d+)/$', views.edit_complete_todo, name='edit_todo'),

]
