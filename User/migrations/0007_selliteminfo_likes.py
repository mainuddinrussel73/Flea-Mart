# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-19 11:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0006_auto_20171118_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='selliteminfo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='item_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
