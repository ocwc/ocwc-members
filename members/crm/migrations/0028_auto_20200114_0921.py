# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-14 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crm", "0027_auto_20190920_0824")]

    operations = [
        migrations.AlterField(
            model_name="membershipapplication",
            name="institution_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (b"secondary-ed", b"Primary and secondary (K-12)"),
                    (b"college", b"Community, technical, or vocational college"),
                    (b"higher-ed", b"University"),
                    (b"non-accredited", b"Informal non-accredited education"),
                    (b"lifelong", b"Lifelong learning"),
                    (b"consortium", b"Consortia"),
                    (b"initiative", b"Open initiatives or special project"),
                    (b"commercial", b"Corporate enterprise"),
                    (b"npo", b"Non-profits, NGO\xe2\x80\x99s, IGO"),
                    (b"cultural", b"Cultural organization"),
                    (b"gov", b"Government"),
                ],
                default=b"",
                max_length=25,
                verbose_name=b"Institution Category",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="institution_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (b"secondary-ed", b"Primary and secondary (K-12)"),
                    (b"college", b"Community, technical, or vocational college"),
                    (b"higher-ed", b"University"),
                    (b"non-accredited", b"Informal non-accredited education"),
                    (b"lifelong", b"Lifelong learning"),
                    (b"consortium", b"Consortia"),
                    (b"initiative", b"Open initiatives or special project"),
                    (b"commercial", b"Corporate enterprise"),
                    (b"npo", b"Non-profits, NGO\xe2\x80\x99s, IGO"),
                    (b"cultural", b"Cultural organization"),
                    (b"gov", b"Government"),
                ],
                default=b"",
                max_length=25,
            ),
        ),
    ]
