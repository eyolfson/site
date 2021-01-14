# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_aur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('package', models.ForeignKey(to_field='id', to='django_aur.Package', on_delete=models.CASCADE)),
                ('version', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': set([('package', 'version')]),
                'db_table': 'aur_update',
                'ordering': ['package', '-timestamp'],
                'get_latest_by': 'timestamp',
            },
            bases=(models.Model,),
        ),
    ]
