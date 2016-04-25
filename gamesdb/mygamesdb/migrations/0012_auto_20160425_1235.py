# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0011_remove_game_fanart_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='ins_creator',
            field=models.TextField(default='admin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='ins_creator',
            field=models.TextField(default='admin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='ins_creator',
            field=models.TextField(default='admin'),
            preserve_default=False,
        ),
    ]
