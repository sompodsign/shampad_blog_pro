from django.contrib import admin
from .models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'rating')
    list_filter = ('active', 'year', 'rating')
    search_fields = ('title',)
