from django.shortcuts import render, redirect
from django.views import generic

from iptcEditor import models
from exif import Image
from .forms import ImageForm


class ImageListView(generic.ListView):
    model = models.Image
    context_object_name = 'image_list'
    template_name = 'iptcEditor/index.html'


class ImageUpdateView(generic.UpdateView):
    model = models.Image
    form_class = ImageForm
    success_url = '/'
