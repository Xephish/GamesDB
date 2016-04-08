# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0002_auto_20160405_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to=b'mygames', blank=True),
        ),
    ]
