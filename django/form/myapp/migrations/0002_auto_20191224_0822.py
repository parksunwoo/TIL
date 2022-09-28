# Generated by Django 2.0.13 on 2019-12-24 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('ip', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
