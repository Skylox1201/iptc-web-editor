from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Image's title",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Image
        fields = {
            "title",
        }
