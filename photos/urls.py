from django.urls import path

from .views import ListPhoto, UpdatePhoto, BatchPhoto

urlpatterns = [
    path('list/', ListPhoto.as_view(), name='list'),
    path('update/<int:pk>/', UpdatePhoto.as_view(), name='update'),
    path('batch/', BatchPhoto.as_view(), name='batch')
]
