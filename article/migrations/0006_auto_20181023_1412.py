# Generated by Django 2.0 on 2018-10-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20181023_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=True),
        ),
    ]