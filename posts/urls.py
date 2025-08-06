from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('post/create', views.PostCreateView.as_view(), name="create_post"),


]
