from django.urls import path, re_path
from . import views

app_name = 'polls'
urlpatterns = [
	re_path(r'^$', views.QuestionListView.as_view(), name="index"),
	re_path(r'^(?P<pk>[0-9]+)/$', views.QuestionView.as_view(), name="vote"),
]
