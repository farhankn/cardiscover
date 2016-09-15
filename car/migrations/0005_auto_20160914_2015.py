# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20160914_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carname',
            name='bodytype',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='cardheko',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='cartrade',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='fueltype',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='imageUrl',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carname',
            name='youtubeurl',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
