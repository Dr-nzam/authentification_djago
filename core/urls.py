from django.urls import path
from .views import register,connexion,index


urlpatterns = [
    path('register', register, name='register'),
    path('login', connexion, name='login'),
    path('index', index , name='index')
]
