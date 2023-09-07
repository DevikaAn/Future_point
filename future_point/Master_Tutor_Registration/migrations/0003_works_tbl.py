# Generated by Django 3.2 on 2021-05-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_Tutor_Registration', '0002_notes_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.FileField(upload_to='works')),
                ('wt', models.CharField(max_length=100)),
                ('wdt', models.DateField()),
                ('course', models.CharField(max_length=100)),
                ('std', models.CharField(max_length=100)),
            ],
        ),
    ]
