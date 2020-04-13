"""Platzigram URLs module"""

#Djangoo
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


#Views
#from platzigram import views as local_views

#URLs


urlpatterns = [

    path('admin/', admin.site.urls),

    # path('hello-world', local_views.hello_world, name='hello_world'),
    # path('sorted/', local_views.sort_int, name='sort'),
    # path('hi/<str:name>/>int:age>/', local_views.say_hi, name='hi'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
