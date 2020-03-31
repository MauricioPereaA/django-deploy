"""Platzigram URLs module"""

#Djangoo
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from platzigram import views as local_views
from posts import views as post_views
from users import views as user_views






urlpatterns = [
    path(r'admin/', admin.site.urls),

    path('hello-world', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort_int, name='sort'),
    path('hi/<str:name>/>int:age>/', local_views.say_hi, name='hi'),

    path('posts/', post_views.list_posts, name='feed'),

    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/signup/', user_views.signup, name='signup')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)