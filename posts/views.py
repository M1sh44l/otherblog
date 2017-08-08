from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
	object_list = Post.objects.all()
	paginator = Paginator(object_list, 10)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	context = {
		"post_list": objects,
		"title": "List",
	}
	return render(request, "post_list.html", context)


def post_detail(request, post_slug):
	object_detail = get_object_or_404(Post, slug=post_slug)
	context = {
		"title": "Detail",
		"object_detail": object_detail,
	}
	return render(request, "post_detail.html", context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Sucessfully created!")
		return redirect("posts:list")
	context = {
		"title": "Create",
		"form": form,
	}
	return render(request, 'post_create.html', context)

def post_update(request, post_slug):
	instance = get_object_or_404(Post, slug=post_slug)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect(instance.get_absolute_url())
	context = {
	"form": form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_slug):
	one_object = get_object_or_404(Post, slug=post_slug)
	one_object.delete()
	messages.success(request, "Successfully deleted!")
	return redirect("posts:list")










