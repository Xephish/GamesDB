# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0007_auto_20160408_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='id_developer',
        ),
        migrations.AlterField(
            model_name='developer',
            name='id',
            field=models.TextField(unique=True, serialize=False, primary_key=True),
        ),
    ]
