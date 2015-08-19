# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('year', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to=b'car')),
            ],
        ),
        migrations.CreateModel(
            name='Car_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consump', models.FloatField(null=True)),
                ('cylinders', models.IntegerField(null=True)),
                ('disp', models.FloatField(null=True)),
                ('bhp', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('accel', models.FloatField(null=True)),
                ('car', models.OneToOneField(to='main.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('car_review', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(to='main.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='origin',
            field=models.ForeignKey(to='main.Origin', null=True),
        ),
    ]
