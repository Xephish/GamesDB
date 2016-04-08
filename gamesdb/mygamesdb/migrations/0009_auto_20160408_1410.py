# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygamesdb', '0008_auto_20160408_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='list_of_games',
            new_name='founder',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='list_of_platforms',
            new_name='fundation_year',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='publisher',
            new_name='website',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='maxcontrollers',
            new_name='generation',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='manufacuturer',
            new_name='manufacturer',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='media',
            new_name='website',
        ),
        migrations.RemoveField(
            model_name='game',
            name='similar_count',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='overview',
        ),
        migrations.AddField(
            model_name='developer',
            name='videogame_genere_preferences',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='website',
            field=models.TextField(null=True, blank=True),
        ),
    ]
