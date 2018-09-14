from django.conf.urls import url, include
from . import views

app_name = 'log'
urlpatterns = [
	url(r'^register/', views.RegisterView, name='register'),
	url(r'^retrieve/$', views.retrieve, name='retrieve'),
]
