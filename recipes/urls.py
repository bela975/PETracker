from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
# from . import settings
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView
from .views import kanban


app_name = 'recipes'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pet/', views.Pet, name='pet'),
    path('pet/register/', views.register_pet, name='register_pet'),
    path('pet/register/submit', views.set_pet, name='set_pet'),
    path('', RedirectView.as_view(url='/pet')),
    path('home/', views.home, name='home'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('kanban/', kanban, name='kanban'),
    path('medicine/', views.medicine, name='medicine'),
    path('home/<int:id>', views.alergy_detail, name='alergy_detail'),
    path('home/delete/<int:id>', views.delete_alergy, name='delete_alergy'),
    path('medicine/<int:id>', views.medicine_detail, name='medicine_detail'),
    path('medicine/delete/<int:id>', views.delete_medicine, name='delete_medicine'),
]
    
# path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)