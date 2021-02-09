from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todos'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('delete_todo/<int:id>', views.delete_todo),
    path('change_todo/<int:id>/<str:status>', views.change_todo),
]
