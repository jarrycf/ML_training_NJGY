# Generated by Django 2.2.13 on 2021-05-08 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('danjia', models.IntegerField()),
                ('xiaoqu', models.CharField(max_length=128)),
                ('quyu', models.CharField(max_length=128)),
                ('huxing', models.CharField(max_length=128)),
                ('mianji', models.FloatField()),
                ('img', models.TextField()),
            ],
            options={
                'verbose_name_plural': '房源',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('tel', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.CreateModel(
            name='See',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField(default=1)),
                ('hid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.House')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'verbose_name_plural': '浏览表',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.House')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'verbose_name_plural': '收藏',
            },
        ),
    ]
