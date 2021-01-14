# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

from django.db import models
from django.urls import reverse

class Post(models.Model):
    content = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=80)
    title = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    class Meta:
        get_latest_by = 'date'
        ordering = ['-date']
