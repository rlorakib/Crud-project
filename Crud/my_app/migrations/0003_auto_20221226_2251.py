# Generated by Django 3.2.16 on 2022-12-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20221226_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registration',
            field=models.CharField(default=1, max_length=33),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]