# Generated by Django 4.0.6 on 2022-07-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meshub', '0003_followerscount_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isAdmin',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
