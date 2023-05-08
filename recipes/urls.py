from django.urls import path, re_path, include

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
# from . import settings
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView
from .views import kanban

app_name = 'recipes'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pet/', views.pet, name='pet'),
    path('pet/register/', views.register_pet, name='register_pet'),
    path('pet/register/submit', views.set_pet, name='set_pet'),
    path('', RedirectView.as_view(url='/pet')),
    path('home/', views.home, name='home'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('kanban/', kanban, name='kanban'),
    # path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)