from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import re
# Create your models here.

def check_if_quest(question_text):
	if re.search('\?\Z', question_text) is None:
		raise ValidationError("Please write a question")

def nbr_limit(answer):
	if answer > 1:
		raise ValidationError("One vote at a time")

class Question(models.Model):
	question_text = models.CharField(
		max_length=200 ,
		validators = [check_if_quest],
	)
	pub_date = models.DateTimeField('published date')
	answer_y = models.IntegerField(default=0, validators=[nbr_limit])
	answer_n = models.IntegerField(default=0, validators=[nbr_limit])
	choices = (
		('Yes'),
		('No'),
	)
	def __str__(self):
		return self.question_text

	def check_published_date(self):
		now = timezone.now()
		return now - datetime.timedelta(id=1) <= self.pub_date <= now
