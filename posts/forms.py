from django import forms
from django.forms import inlineformset_factory
from . import models
from django.forms.widgets import ClearableFileInput



class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True


class PostForm(forms.ModelForm):
    
    class Meta:
        model = models.Post
        fields = ("content",)
        widgets = {
            "content": forms.TextInput(attrs={'class':'form-control rounded'})
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = models.Image
        fields = ['image']


ImageFormSet = inlineformset_factory(models.Post, 
                                    models.Image,
                                    form=ImageForm, 
                                    extra=1,
                                    can_delete=False)
