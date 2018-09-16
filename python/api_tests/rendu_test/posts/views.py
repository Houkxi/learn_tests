from .models import Posts
from .serializers import PostSerializer, PostDetailSerializer
from django.utils import timezone
from rest_framework import generics
from django.shortcuts import redirect

# Create your views here.

def redirect_url(request):
	response = redirect('/posts/')
	return response

# GET command
class ListView(generics.ListAPIView):
	queryset = Posts.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
	serializer_class = PostSerializer

# POST command
class CreatePostView(generics.CreateAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostDetailSerializer


# GET by <id>, PUT & DELETE
class DetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Posts.objects.filter(pub_date__lte=timezone.now())
	serializer_class = PostDetailSerializer
