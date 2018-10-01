# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-01 06:31
from __future__ import unicode_literals

from django.db import migrations, models


def forwards(apps, schema_editor):
    Organization = apps.get_model("crm", "Organization")

    for org in Organization.objects.filter(associate_consortium='TOCWC'):
        org.associate_consortium = 'TOCEC'
        org.save()

class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20180726_0207'),
    ]

    operations = [
        migrations.RunPython(forwards, hints={'target_db': 'default'}),
        migrations.AlterField(
            model_name='membershipapplication',
            name='associate_consortium',
            field=models.CharField(blank=True, choices=[(b'CCCOER', b'Community College Consortium for Open Educational Resources (CCCOER)'), (b'CORE', b'CORE'), (b'JOCWC', b'Japan OCW Consortium'), (b'KOCWC', b'Korea OCW Consortium'), (b'TOCEC', b'Taiwan Open Course and Education Consortium'), (b'Turkish OCWC', b'Turkish OpenCourseWare Consortium'), (b'UNIVERSIA', b'UNIVERSIA'), (b'FOCW', b'OCW France'), (b'OTHER', b'OTHER')], default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='associate_consortium',
            field=models.CharField(blank=True, choices=[(b'CCCOER', b'Community College Consortium for Open Educational Resources (CCCOER)'), (b'CORE', b'CORE'), (b'JOCWC', b'Japan OCW Consortium'), (b'KOCWC', b'Korea OCW Consortium'), (b'TOCEC', b'Taiwan Open Course and Education Consortium'), (b'Turkish OCWC', b'Turkish OpenCourseWare Consortium'), (b'UNIVERSIA', b'UNIVERSIA'), (b'FOCW', b'OCW France'), (b'OTHER', b'OTHER')], default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='initiative_title1',
            field=models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Initiative 1 Title'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='initiative_title2',
            field=models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Initiative 2 Title'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='initiative_title3',
            field=models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Initiative 3 Title'),
        ),
    ]
