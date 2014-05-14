# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_aur', '0002_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='is_available',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
