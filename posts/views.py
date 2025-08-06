from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.PostForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user  
        self.object = form.save()
        for uploaded_file in self.request.FILES.getlist('images-0-image'):
            models.Image.objects.create(post=self.object, image=uploaded_file)
        return render(self.request, "accounts/components/_post.html", {"post": self.object})

    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile/timeline.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    
    def get_queryset(self):
        # Fetch the user + profile in one query
        return (
            super()
            .get_queryset()
            .select_related("profile")  # join with profile
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.object

        # Fetch posts + images + author's profile in one query per table
        posts = (
            models.Post.objects.filter(user=profile_user)
            .order_by("-created_at")
            .select_related("user",)  # author + author profile
            .prefetch_related("images")  # all images in one query
        )

        context.update({
            "profile_user": profile_user,
            "posts": posts,
            "form": forms.PostForm(),
            "formset": forms.ImageFormSet(),
        })
        return context
