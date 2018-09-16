# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

# Make sure only the parents are posted
class PostsManager(models.Manager):
	def all(self):
		qs = super(PostsManager, self).filter(parent=None)
		return qs

class Posts(models.Model):
	post_text = models.TextField()
	pub_date = models.DateField(auto_now_add=True)
	parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

	objects = PostsManager()

	def children(self):
		return Posts.objects.filter(parent=self)
	def is_parent(self):
		if self.parent is not None:
			return False
		return True

class Comments(models.Model):
	# post_key = models.ForeignKey(Posts, null=True, related_name='coms', on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=50)
	publisher_name = models.CharField(max_length=15)
