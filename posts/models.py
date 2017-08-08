from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	image = models.ImageField(null=True, blank=True, upload_to="post_images")
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)

	class Meta:
		ordering = ["-timestamp", "-updated"]


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"post_slug": self.slug})



def create_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug = slugify(instance.title)
		qs = Post.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s"%(slug, instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(create_slug, sender=Post)


	# def create_slug(instance, new_slug=None):
	# 	slug = slugify(instance.title)
	# 	if slug is not None:
	# 		slug = new_slug
	# 	exists = Post.objects.filter(slug=slug).exists()
	# 	if exists:
	# 		new_slug = "%s-%s"%(slug, instance.id)
	# 		return create_slug(instance, new_slug=new_slug)
	# 	return slug



