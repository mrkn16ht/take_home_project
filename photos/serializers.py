from rest_framework import serializers
from photos.models import Photo
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin, ListBulkCreateUpdateDestroyAPIView


class PhotoSerializer(serializers.ModelSerializer):
    publishing_date = serializers.DateTimeField(required=False)

    class Meta:
        model = Photo
        fields = ('id', 'user', 'caption', 'status', 'publishing_date', 'photo_file')


class BatchPhotoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Photo
        list_serializer_class = BulkListSerializer
        fields = ('id', 'user', 'caption', 'status', 'publishing_date', 'photo_file')