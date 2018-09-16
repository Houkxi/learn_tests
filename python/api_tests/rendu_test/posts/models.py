from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

def time_stamps(date):
	if date < timezone.now():
		raise ValidationError("Please write a valid date")

class Posts(models.Model):
	username = models.CharField(max_length=20)
	post_text = models.TextField()
	pub_date = models.DateTimeField(timezone.now(), validators=[time_stamps])
	last_update = models.DateTimeField(auto_now_add=True)

	def was_published_at(self):
		now = timezone.now()
		return self.pub_date <= now
