from rest_framework import serializers
from .models import Posts

# What will show between the different views

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = [
			'post_text',
			'id',
		]

class PostDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = [
			'username',
			'post_text',
			'pub_date',
			'last_update',
			'id',
		]
