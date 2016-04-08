# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0009_auto_20160408_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='trailer',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
