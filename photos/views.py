from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from photos.models import Photo
from photos.serializers import PhotoSerializer, BatchPhotoSerializer


class PhotoFilter(FilterSet):
    class Meta:
        model = Photo
        fields = ['status', 'user']


class ListPhoto(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = PhotoFilter
    ordering_fields = ['publishing_date']
    template_name = 'list_photo.html'


class UpdatePhoto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class BatchPhoto(ListBulkCreateUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = BatchPhotoSerializer