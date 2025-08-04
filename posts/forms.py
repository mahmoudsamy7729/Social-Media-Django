from django import forms
from django.forms import inlineformset_factory
from . import models


class PostForm(forms.ModelForm):
    
    class Meta:
        model = models.Post
        fields = ("content",)
        widgets = {
            "content": forms.TextInput(attrs={'class':'form-control rounded'})
        }
ImageFormSet = inlineformset_factory(models.Post, 
                                    models.Image,
                                    fields=['image'], 
                                    extra=1,
                                    can_delete=False)
