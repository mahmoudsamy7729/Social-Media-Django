from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/post', views.PostCreateView.as_view(), name="create_post")
]
