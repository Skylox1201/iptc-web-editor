from django import forms
from iptcEditor import models
import pyexiv2
from django.conf import settings


class ImageForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Image's description",
                "class": "form-control",
            }
        ),
        label={
            'name': 'Title'
        }
    )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Image's title",
                "class": "form-control",
            }
        ),
        label={
            'name': 'Description'
        }
    )

    class Meta:
        model = models.Image
        fields = (
            "title",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the ImageDescription Metadata from the image
        current_image_path = settings.MEDIA_ROOT + self.instance.image.name
        with pyexiv2.Image(current_image_path, encoding='utf-8') as img:
            # Set the textarea value to the current value
            self.fields['description'].initial = img.read_iptc().get('Iptc.Application2.ObjectName')


class UploadImage(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
        label={
            'name': 'Title'
        }
    )

    image = forms.FileField(
        required=True,
        widget=forms.widgets.FileInput(
            attrs={
                "class": "form-control",
            }
        ),
        label={
            'name': 'Image'
        }
    )

    class Meta:
        model = models.Image
        fields = (
            "title", "image",
        )
