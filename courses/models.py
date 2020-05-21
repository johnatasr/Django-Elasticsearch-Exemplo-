from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    course_id = models.IntegerField(_('course_id'),)
    course_title = models.CharField(_('course_title'), max_length=480,)
    url = models.CharField(_('url'), max_length=480,)
    is_paid = models.BooleanField(_('is_paid'), max_length=480,)
    price = models.IntegerField(_('price'),)
    num_subscribers = models.IntegerField(_('num_subscribers'),)
    num_reviews = models.IntegerField(_('num_reviews'),)
    num_lectures = models.IntegerField(_('num_lectures'),)
    level = models.CharField(_('level'), max_length=480, )
    content_duration = models.CharField(_('content_duration'), max_length=255, )
    published_timestamp = models.DateTimeField(_('published_timestamp'))
    subject = models.CharField(_('subject'), max_length=255,)

    def __str__(self):
        return str(self.id)

    def get_title(self):
        return '{} - Type: {}'.format(self.course_title, self.subject)

