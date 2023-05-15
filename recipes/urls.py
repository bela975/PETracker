from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView
from .views import kanban

app_name='recipes'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pet/', views.pet, name='pet'),
    path('pet/register/', views.register_pet, name='register_pet'),
    path('pet/register/submit', views.set_pet, name='set_pet'),
    path('', RedirectView.as_view(url='/pet')),
    path('home/<int:pet_id>', views.home, name='home'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event'),
    #re_path(r'^event/delete/(?P<event_id>\d+)/$', views.event_delete, name='event_delete'),
    path('kanban/', kanban, name='kanban'),
    path('medicine/', views.medicine, name='medicine'),
    path('home/<int:id>', views.alergy_detail, name='alergy_detail'),
    path('home/delete/<int:id>', views.delete_alergy, name='delete_alergy'),
    path('medicine/<int:id>', views.medicine_detail, name='medicine_detail'),
    path('medicine/delete/<int:id>', views.delete_medicine, name='delete_medicine'),


]

