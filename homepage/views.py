from django.shortcuts import render
from django.utils.html import strip_tags
from blog.models import Post


# Create your views here.
def home_page(request):
    posts = Post.published.all()[:3]
    return render(request, 'index.html', {
        'posts': posts,
    })
