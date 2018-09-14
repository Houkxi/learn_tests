from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(request, pk=1), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote', views.vote, name='vote'),
	url(r'^ideas', views.ideas, name='ideas'),
	url(r'^input_question', views.input_question, name='input_question')
 ]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# """Function enables a wider range of query strings
# (e.g. http://127.0.0.1:8000/api/v1/users/1.json)
# """
#
# urlpatterns = format_suffix_patterns(urlpatterns)
