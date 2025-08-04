from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, login
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView, TemplateView, View, CreateView
from django.urls import reverse_lazy
from . import forms, models


class RegisterView(CreateView):
    template_name = "accounts/auth/register.html"
    model = User
    form_class = forms.RegisterionForm
    success_url = reverse_lazy('accounts:edit_profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@require_POST
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

class ProfileEditView(LoginRequiredMixin, View):
    template_name = "accounts/profile/edit.html"

    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render (request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile', username=request.user.username)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })
    
class ProfileAboutView(DetailView):
    model = User
    template_name = "accounts/profile/about.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'