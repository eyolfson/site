# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

from django.db import models

class Post(models.Model):
    content = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=80)
    title = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('blog:post', (), {'slug': self.slug})

    class Meta:
        get_latest_by = 'date'
        ordering = ['-date']
