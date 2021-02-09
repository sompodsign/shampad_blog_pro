from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('books/', include('library.urls', namespace='books')),
    path('movie/', include('movie.urls', namespace='movie')),
    path('', include('homepage.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
    path('account/', include('django.contrib.auth.urls')),
    path('tools/', include('amazon.urls', namespace='amazon')),
    path('tools/todos/', include('todo.urls', namespace='todo')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), # to serve media
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
