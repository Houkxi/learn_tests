from rest_framework import serializers
from .models import Question

class QuestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('question_text', 'pub_date')

class YesOrNo(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('question_text', 'answer_n', 'answer_y', 'choices')
