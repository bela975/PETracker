from django.urls import path, re_path
from . import views 

app_name = 'recipes'
urlpatterns = [
    path('',views.login_user, name="login"),
    path('home_choose_pet/', views.home_choose_pet, name="home"),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_pet/', views.register_pet, name='register_pet'),
    path('home_pet/', views.pet_home, name="home_pet"),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),

    path('medicine/', views.medicine_page, name='medicine_page'),
    path('medicine/<int:id>', views.medicine_detail, name='medicine_detail'),
    path('medicine/delete/<int:id>', views.delete_medicine, name='delete_medicine'),

    path('todo/<int:id>', views.todo_detail, name='todo_detail'),
    path('todo/delete/<int:id>', views.delete_todo, name='delete_todo'),

    path('food/', views.food, name='food'),
    path('food/<int:id>', views.food_detail, name='food_detail'),
    path('food/delete/<int:id>', views.delete_food, name='delete_food'),
    path('home_pet/<int:id>', views.alergy_detail, name='alergy_detail'),
    path('home_pet/delete/<int:id>', views.delete_alergy, name='delete_alergy'),
    path('kanban/', views.kanban, name='kanban'),
    path('add_task/', views.add_task, name='add_task'),
    path('remove_task/<int:task_id>/', views.remove_task, name='remove_task'),
    path('move_task/<int:task_id>/', views.move_task, name='move_task'),
    path('kanban/<str:show_history>/', views.kanban, name='kanban'),
    path('restore_task/<int:task_id>/', views.restore_task, name='restore_task'),
    path('move_task_back/<int:task_id>/', views.move_task_back, name='move_task_back'),

    #path('todo/', views.medicine_page, name='medicine_plan'),
    #path('todo/<int:id>', views.todo_detail, name='medicine_plan_detail'),
    #path('todo/delete/<int:id>', views.delete_todo, name='delete_medicine_from_plan'),
]
