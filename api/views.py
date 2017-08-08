from django.shortcuts import render
from rest_framework.generics import ListAPIView
from posts.models import Post

# Create your views here.
class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	lookup_ur_kwargs = 'post_slug'
