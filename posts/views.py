from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import ListView, CreateView, DetailView
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
        formset = forms.ImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        if formset.is_valid():
            formset.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            'accounts:profile',
            kwargs={'username': self.request.user.username}
        )
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile/timeline.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.object
        context['posts'] = models.Post.objects.filter(user = profile_user).order_by('-created_at')
        context['form'] = forms.PostForm()
        context['formset'] = forms.ImageFormSet()
        return context

