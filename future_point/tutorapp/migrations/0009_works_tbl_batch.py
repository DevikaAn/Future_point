# Generated by Django 4.0.5 on 2022-10-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0008_videoclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='works_tbl',
            name='batch',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
