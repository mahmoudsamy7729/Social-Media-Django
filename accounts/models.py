from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from . import AccountsUtils


# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True, unique=False)
    profile_photo = models.ImageField(upload_to=AccountsUtils.profile_image_path, blank=True, default='profile_pics/default.webp')
    cover_photo = models.ImageField(upload_to=AccountsUtils.cover_image_path, blank=True, default='cover_pics/default.webp')
    address = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"