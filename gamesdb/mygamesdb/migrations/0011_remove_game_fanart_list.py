# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0010_auto_20160408_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='fanart_list',
        ),
    ]
