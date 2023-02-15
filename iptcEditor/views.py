from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from iptcEditor import models
from PIL import Image
from .forms import ImageForm, UploadImage
import pyexiv2
from django.contrib.messages.views import SuccessMessageMixin


# Afficher la liste des images
class ImageListView(generic.ListView):
    model = models.Image
    context_object_name = 'image_list'
    template_name = 'iptcEditor/index.html'


# Mettre à jour une image
class ImageUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = models.Image
    form_class = ImageForm
    success_url = '/'
    success_message = 'Successfully updated!'

    def form_valid(self, form):
        # Get the image to update
        instance = form.save(commit=False)

        # get the new image description
        new_description = form.cleaned_data['description']

        # set the new ImageDescription Metadata from the image
        current_image_path = instance.image.file.name
        current_image = pyexiv2.Image(current_image_path)
        current_image.modify_iptc({'Iptc.Application2.ObjectName': new_description})

        response = {'msg': 'Submited Successfully',
                    'url': reverse('index'),
                    'created': True}

        return super().form_valid(form)


class ImageCreateView(SuccessMessageMixin, generic.CreateView):
    model = Image
    form_class = UploadImage
    template_name = "iptcEditor/image_upload.html"
    success_url = reverse_lazy("index")
    success_message = 'Successfully created!'
