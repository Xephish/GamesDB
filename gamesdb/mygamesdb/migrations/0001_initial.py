# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_developer', models.TextField()),
                ('developer_name', models.TextField()),
                ('list_of_games', models.TextField(null=True, blank=True)),
                ('list_of_platforms', models.TextField(null=True, blank=True)),
                ('average_videogames_rating', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('game_title', models.TextField()),
                ('release_date', models.TextField(null=True, blank=True)),
                ('ESRB', models.TextField(null=True, blank=True)),
                ('generes', models.TextField(null=True, blank=True)),
                ('trailer', models.TextField(null=True, blank=True)),
                ('publisher', models.TextField(null=True, blank=True)),
                ('rating', models.TextField(null=True, blank=True)),
                ('similar_count', models.TextField(null=True, blank=True)),
                ('fanart_list', models.TextField(null=True, blank=True)),
                ('updates', models.TextField(null=True, blank=True)),
                ('developer', models.ForeignKey(default=1, to='mygamesdb.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('console_name', models.TextField()),
                ('controller', models.TextField(null=True, blank=True)),
                ('overview', models.TextField(null=True, blank=True)),
                ('manufacuturer', models.TextField(null=True, blank=True)),
                ('cpu', models.TextField(null=True, blank=True)),
                ('memory', models.TextField(null=True, blank=True)),
                ('graphics', models.TextField(null=True, blank=True)),
                ('sound', models.TextField(null=True, blank=True)),
                ('display', models.TextField(null=True, blank=True)),
                ('media', models.TextField(null=True, blank=True)),
                ('maxcontrollers', models.TextField(null=True, blank=True)),
                ('rating', models.TextField(null=True, blank=True)),
                ('images', models.TextField(null=True, blank=True)),
                ('developer', models.ForeignKey(default=1, to='mygamesdb.Developer')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(default=1, to='mygamesdb.Platform'),
        ),
    ]
