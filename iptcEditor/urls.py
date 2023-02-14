from django.urls import path

from . import views

urlpatterns = [
    path('', views.ImageListView.as_view(), name='index'),
    path('update/<int:pk>', views.ImageUpdateView.as_view(), name='image_update'),
]
