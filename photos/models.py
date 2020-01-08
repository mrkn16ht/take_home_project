from django.db import models
from django.core.exceptions import ValidationError
from users.models import CustomUser
from django.core.files.images import get_image_dimensions


def validate_image_size(image):
    image_size = image.size
    image_width, image_height = get_image_dimensions(image.file)
    print(image_width)
    print(image_height)
    max_size = 2621440
    max_height = 1280
    max_width = 1024
    if image_size > max_size:
        raise ValidationError('Please upload photo smaller than 2.5 MB')
    if image_height > max_height:
        raise ValidationError('Please upload photo with Height less than 1280 pixels')
    if image_width > max_width:
        raise ValidationError('Please upload photo with Width less than 1024 pixels')


STATUS_CHOICES = (
    ('Posted', 'Posted'),
    ('Draft', 'Draft')
)


class Photo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='User')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='Caption')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, blank=False, verbose_name='Status')
    publishing_date = models.DateTimeField(null=True, blank=True, verbose_name='Publishing Date', )
    photo_file = models.ImageField(upload_to='images/', blank=False, null=True, validators=[validate_image_size],
                                   verbose_name='Photo File')

    def __str__(self):
        return self.caption
