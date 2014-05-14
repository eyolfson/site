# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arch',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'aur_arch',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('arch', models.ForeignKey(to_field='id', to='django_aur.Arch')),
                ('name', models.CharField(db_index=True, max_length=64)),
            ],
            options={
                'unique_together': set([('name', 'arch')]),
                'db_table': 'aur_package',
                'ordering': ['name', 'arch'],
            },
            bases=(models.Model,),
        ),
    ]
