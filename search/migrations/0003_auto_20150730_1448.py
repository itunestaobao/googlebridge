# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_search_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search_data',
            old_name='timesamp',
            new_name='sd_timesamp',
        ),
    ]
