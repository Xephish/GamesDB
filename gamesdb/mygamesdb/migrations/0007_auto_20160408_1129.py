# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0006_auto_20160408_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='images',
        ),
        migrations.AddField(
            model_name='developer',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
    ]
