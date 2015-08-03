# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sd_keyword', models.CharField(max_length=200)),
                ('sd_start', models.CharField(max_length=200)),
                ('sd_title', models.TextField()),
                ('sd_url', models.TextField()),
                ('sd_content', models.TextField()),
                ('sd_count', models.CharField(max_length=200)),
                ('timesamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
