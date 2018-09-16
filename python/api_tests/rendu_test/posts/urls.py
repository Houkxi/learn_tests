from django.urls import re_path
from . import views

urlpatterns = [
	# Url Pattern for the entire list
	re_path(r'^$', views.ListView.as_view(), name='List'),
	# Url Pattern to create next post
	re_path(r'^create/$', views.CreatePostView.as_view(), name='Post'),
	# Url Pattern redirection after creating something, just in case
	re_path(r'^create/[0-9]+/$', views.redirect_url),
	# Url Pattern forallkind of updates to a post
	re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='Detail'),
]
