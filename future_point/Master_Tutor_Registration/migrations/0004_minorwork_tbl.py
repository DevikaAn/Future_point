# Generated by Django 3.2 on 2021-05-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_Tutor_Registration', '0003_works_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='minorwork_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.CharField(max_length=100)),
                ('adt', models.DateTimeField(auto_now=True)),
                ('assignment', models.FileField(upload_to='mwork')),
                ('stdcrs', models.CharField(max_length=100)),
                ('stdname', models.CharField(max_length=100)),
            ],
        ),
    ]
