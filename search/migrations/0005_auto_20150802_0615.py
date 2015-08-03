# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20150731_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fb_words',
            name='fb_word',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='search_data',
            name='sd_keyword',
            field=models.TextField(),
        ),
    ]
