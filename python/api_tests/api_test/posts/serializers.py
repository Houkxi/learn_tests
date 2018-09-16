from rest_framework import serializers
from .models import Posts, Comments


# def parent_or_not(parent_id=None):

class PostSerializer(serializers.ModelSerializer):
	# coms = serializers.StringRelatedField(many=True)
	reply_count = serializers.SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
			'id',
			'post_text',
			'pub_date',
			'reply_count',
			'parent'
		]
	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

class ChildSerializer(serializers.ModelSerializer):
	# coms = serializers.StringRelatedField(many=True)
	class Meta:
		model = Posts
		fields = [
			'id',
			'post_text',
			'pub_date',
			'parent'
		]

class CommentDetailSerializer(serializers.ModelSerializer):
	# coms = serializers.PrimaryKeyRelatedField(many=True, queryset=Comments.objects.all())
	reply_count = serializers.SerializerMethodField()
	replies = serializers.SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
			'id',
			'post_text',
			'pub_date',
			'replies',
			'reply_count',
		]
	def get_replies(self, obj):
		if obj.is_parent:
			return ChildSerializer(obj.children(), many=True).data
		return None
	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0
