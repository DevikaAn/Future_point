# Generated by Django 4.0.5 on 2022-10-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0009_works_tbl_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works_tbl',
            name='batch',
        ),
        migrations.AddField(
            model_name='notes_tbl',
            name='batch',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
