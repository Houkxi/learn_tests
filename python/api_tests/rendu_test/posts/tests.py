from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
import datetime
from .models import Posts

# Create your tests here.

class PostsModelTests(TestCase):

	def test_was_published_at_with_future_question(self):
		"""
		was_published_at() returns False for posts whose pub_date
		is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Posts(pub_date=time)
		self.assertIs(future_question.was_published_at(), False)
