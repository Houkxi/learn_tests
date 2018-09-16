from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
	# url(r'^$', views.CreateView.as_view(), name='Create'),
	url(r'^$', views.ListView.as_view(), name='Index'),
	url(r'^create/$', views.PostCreateView.as_view(), name='Create'),
	url(r'^(?P<pk>[0-9]+)/post/$', views.DetailView.as_view(), name='Post'),
	url(r'^(?P<pk>[0-9]+)/post/child$', views.CommentCreateView.as_view(), name='Comment'),
	# url(r'^(?P<pk>[0-9]+)/post/comment/$', views.CreateCommentView.as_view(), name='Comments'),
	# url(r'^(?P<pk>[0-9]+)/post/comments/$', views.CommentIndexView.as_view(), name='Comment'),
	# url(r'^(?P<pk>[0-9]+)/post/comments/$', views.CommentView.as_view(), name='Comment'),
]
