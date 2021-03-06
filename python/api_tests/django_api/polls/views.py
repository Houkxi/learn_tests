from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from rest_framework import generics
from django.utils import timezone
from .serializers import PollsSerializers
from .models import Choice, Question


class IndexView(generics.RetrieveAPIView):
	queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	serializer_class = PollsSerializers
	look_field = "pk"
	# def preform_create(self, serializer):
	# 	serializer.save()

class DetailView(generics.RetrieveUpdateAPIView):
	queryset = Question.objects.filter(pub_date__lte=timezone.now())
	serializer_class = PollsSerializers


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question':question, 'error_message': 'You didn\'t select a choice'})
	else:
		selected_choice.vote += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def ideas(request):
	return render(request, 'polls/question_form.html', {'error_message': 'Have to input a question'})

def input_question(request):
		question = Question
		question.question_text = request.POST["question"]
		print (question.question_text)
		return HttpResponseRedirect(reverse('polls:ideas'))
