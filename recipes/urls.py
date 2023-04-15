from django.urls import path

from . import views
from .views import todo_list


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pet/', views.perfis_pet, name='perfis_pet'),
    path('todo_list/', views.todo_list, name='todo_list'),
    #path('home/', views.home, name='home')
]