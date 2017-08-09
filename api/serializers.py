from rest_framework import serializers
from posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name="api:detail",
		lookup_field="slug",
		lookup_url_kwarg="post_slug",
		)
	class Meta:
		model = Post
		fields = ['title', 'content', 'slug', 'timestamp', 'detail']

class PostDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ['title', 'content','slug', 'timestamp']

class PostDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post

class PostCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post 
		fields = ['title', 'content']

class PostUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ['title', 'content', 'slug']