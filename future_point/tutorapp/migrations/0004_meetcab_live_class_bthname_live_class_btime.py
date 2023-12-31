# Generated by Django 4.0.3 on 2022-04-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0003_live_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetCab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.CharField(max_length=100)),
                ('btch', models.CharField(max_length=100)),
                ('stdname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='live_class',
            name='bthname',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='live_class',
            name='btime',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
