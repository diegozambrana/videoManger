# Generated by Django 3.1.5 on 2021-01-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20210123_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='show',
            name='coming_soon',
            field=models.BooleanField(default=False),
        ),
    ]
