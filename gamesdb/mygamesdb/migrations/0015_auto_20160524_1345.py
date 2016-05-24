# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mygamesdb', '0014_auto_20160518_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name=b'Rating (stars)', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mygamesdb.Review')),
                ('game', models.ForeignKey(to='mygamesdb.Game')),
            ],
            bases=('mygamesdb.review',),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
