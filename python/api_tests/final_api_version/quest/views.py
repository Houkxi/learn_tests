from django.shortcuts import render
from .models import Question
from .serializers import QuestSerializer, YesOrNo
from rest_framework import generics
from django.utils import timezone
# Create your views here.

class QuestionListView(generics.ListCreateAPIView):
	queryset = Question.objects.filter(pub_date__lte=timezone.now())
	serializer_class = QuestSerializer

	def perform_create(self, serializer):
		serializer.save()

class QuestionView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.filter(pub_date__lte=timezone.now())
	serializer_class = YesOrNo

	# def update(self, instance, validated_data):
	# 	demo = Demo.objects.get(pk=instance.id)
	# 	Demo.objects.filter(pk=instance.id)\
	# 		.update(**validated_data)
	# 	return demo
