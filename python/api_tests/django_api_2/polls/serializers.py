from rest_framework import serializers
from .models import Question, Choice
from django.utils import timezone
import datetime

class PollsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ("question_text", "pub_date", "pk")
