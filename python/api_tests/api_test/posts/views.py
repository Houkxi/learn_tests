# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Posts, Comments
from .serializers import PostSerializer, CommentDetailSerializer, ChildSerializer
from rest_framework import serializers
from rest_framework import generics
from rest_framework.exceptions import APIException
# Create your views here.

class PostCreateView(generics.CreateAPIView):
	model = Posts.objects.all()
	serializer_class = PostSerializer

class ListView(generics.ListAPIView):
	queryset = Posts.objects.all()
	serializer_class = CommentDetailSerializer

class DetailView(generics.RetrieveAPIView):
	queryset = Posts.objects.all()
	serializer_class = CommentDetailSerializer

class CommentCreateView(generics.ListCreateAPIView):
	queryset = Posts.objects.filter(pk=None)
	serializer_class = ChildSerializer
