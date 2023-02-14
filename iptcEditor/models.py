from django.db import models
from django.urls import reverse


class Image(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    # Metadata
    class Meta:
        ordering = ['title']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('image_update', args=[str(self.id)])

    def __str__(self):
        return self.title
