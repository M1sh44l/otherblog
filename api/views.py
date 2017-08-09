from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostDeleteSerializer, PostCreateSerializer, PostUpdateSerializer

# Create your views here.
class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'


class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDeleteSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostUpdateSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'	






