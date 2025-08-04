from django.urls import path
from . import views
from posts.views import ProfileDetailView
from django.contrib.auth.views import LoginView
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',
         LoginView.as_view(template_name="accounts/auth/login.html",
                           authentication_form= LoginForm),
          name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit_profile'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<str:username>/about', views.ProfileAboutView.as_view(), name='profile-about'),
]
