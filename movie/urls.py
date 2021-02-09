from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.watch_now, name='watch_now'),
    path('library/', views.movie_library, name='movie_library'),
    path('custom-filter/', views.custom_filter, name='custom-filter'),
    path('add-item/', views.add_item, name='add_movie'),
    path('edit_movie/<int:id>', views.edit_item, name='edit_movie'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),

]
