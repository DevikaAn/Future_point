# Generated by Django 4.0.5 on 2022-11-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_Tutor_Registration', '0006_notes_tbl_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='works_tbl',
            name='up_date',
            field=models.DateField(auto_now=True),
        ),
    ]
