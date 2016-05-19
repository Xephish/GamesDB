# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0013_auto_20160429_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='city',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='province_or_state',
            field=models.TextField(null=True, blank=True),
        ),
    ]
