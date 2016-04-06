# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='id_developer',
            field=models.TextField(unique=True),
        ),
    ]
