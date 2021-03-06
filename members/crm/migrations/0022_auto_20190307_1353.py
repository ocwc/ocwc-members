# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-03-07 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crm", "0021_auto_20190215_0859")]

    operations = [
        migrations.AlterModelOptions(
            name="billinglog", options={"ordering": ["-pub_date"]}
        ),
        migrations.AlterField(
            model_name="billinglog",
            name="log_type",
            field=models.CharField(
                choices=[
                    (b"create_invoice", b"Invoice"),
                    (b"send_invoice", b"Send invoice via email"),
                    (b"create_paid_invoice", b"Create paid invoice"),
                    (b"send_paid_invoice", b"Send paid invoice via email"),
                    (b"create_note", b"Add a note"),
                    (b"create_payment", b"Payment"),
                ],
                max_length=30,
            ),
        ),
    ]
