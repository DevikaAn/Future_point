# Generated by Django 4.0.3 on 2022-04-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0006_remove_live_class_details_remove_live_class_stdname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendlink',
            name='btime',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sendlink',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
