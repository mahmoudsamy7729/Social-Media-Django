from django.db import models
from django.contrib.auth.models import User
from socialmedia import SharedUtils
from PIL import Image as PILImage

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        indexes = [
            models.Index(fields=["user", "-created_at"]),
        ]

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=SharedUtils.post_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
    # Save image first to get path
        super().save(*args, **kwargs)

        # Open the image file
        img_path = self.image.path
        img = PILImage.open(img_path)

        # Force resize to fixed width & height
        target_size = (621, 400)  # width, height in px
        img = img.resize(target_size, PILImage.LANCZOS)

        # Save optimized
        img.save(img_path, optimize=True, quality=85)

    
    