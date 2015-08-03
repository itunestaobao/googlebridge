# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20150730_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_data',
            name='sd_url',
            field=models.CharField(max_length=64),
        ),
    ]
