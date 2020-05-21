"""Posts URLS"""

#Django
from django.urls import path

#Views
from posts import views

#cache
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


urlpatterns = [
    
    path(
        route='', 
        view=cache_page(CACHE_TTL)(views.PostsFeedView.as_view()), #high order component
        name='feed'
    ),

    path(
        route='posts/new/', 
        view=views.CreatePostView.as_view(), 
        name='create'
    ),

    path(
        route='posts/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
    
]
