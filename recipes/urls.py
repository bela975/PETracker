from django.urls import path, re_path
from . import views 

app_name='recipes'
urlpatterns = [
    path('',views.login_user, name="login"),
    path('home_choose_pet', views.home_choose_pet, name="home"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('register_pet', views.register_pet, name='register_pet'),
    path('home_pet', views.pet_home, name="home_pet"),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('medicine/', views.medicine, name='medicine'),
    path('medicine/<int:id>', views.medicine_detail, name='medicine_detail'),
    path('medicine/delete/<int:id>', views.delete_medicine, name='delete_medicine'),
    path('food/', views.food, name='food'),
    path('food/<int:id>', views.food_detail, name='food_detail'),
    path('food/delete/<int:id>', views.delete_food, name='delete_food'),

]
