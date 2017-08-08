from django.conf.urls import url
from .views import PostListAPIView

urlpatterns = [
	url(r'^list/$', PostListAPIView.as_view(), name="list"),
	
]