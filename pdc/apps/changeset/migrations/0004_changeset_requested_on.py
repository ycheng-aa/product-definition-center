# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0003_changeset_pdc_change_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='changeset',
            name='requested_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 2, 15, 31, 582918, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
