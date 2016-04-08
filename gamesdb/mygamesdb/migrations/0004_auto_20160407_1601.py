# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0003_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
    ]
