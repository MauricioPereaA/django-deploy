"""Users URLs"""

#Django
from django.urls import path, include
from rest_framework import routers


#Views
from users import views

router = routers.DefaultRouter()
router.register(r'listUser', views.UserViewSet) # r de recursive para generar las vistas de los usuarios
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    
    # Management
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),
    
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='signup'
    ),

    path(
        route='me/profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='update'
    ),

    #Posts
    path(
        route='detail/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    #RestViews
    path(
        route='',
        view=include(router.urls),
        name='api'
    ),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
