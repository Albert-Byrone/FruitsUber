# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0005_orderdetials'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='foodtaskerapp.Order')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetials',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='orderdetials',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderDetials',
        ),
    ]