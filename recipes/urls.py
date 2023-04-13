from django.urls import path
from django.conf.urls import url
from . import views

appName = 'PETracker'
urlpatterns = [
    path('', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

