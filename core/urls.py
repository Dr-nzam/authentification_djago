from django.urls import path
from .views import register,index


urlpatterns = [
    path('register', register, name='register'),
    path('index', index , name='index')
]
