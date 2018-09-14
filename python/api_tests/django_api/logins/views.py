from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Logins
from django.views import generic
# Create your views here.

# def index(request, logins_id):
# 	login = get_object_or_404(Logins, pk=logins_id)
# 	return render(request, 'logins/index.html', {'username': login.username, 'password':login.password})

# class IndexView(generic.v):
# 	template_name = 'logins/index.html'
# 	context_object_name = 'logins_list'
# 	def get_queryset(self):
# 		pass

def retrieve(request):
	use = request.post.get('username', none)
	user = Logins.objects.get(username=use)
	return Logins.objects.all()

def RegisterView(request):
	return render(request, 'logins/register.html', {})
