# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carname',
            name='fueltype',
            field=models.CharField(default=datetime.datetime(2016, 9, 7, 12, 6, 58, 577225, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
