# Generated by Django 4.0.3 on 2022-04-27 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Minor_Programmer', '0003_course'),
        ('tutorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dt', models.CharField(max_length=100)),
                ('url', models.FileField(upload_to='notes')),
                ('crs', models.CharField(max_length=100)),
                ('std', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
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
        migrations.CreateModel(
            name='appre_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studname', models.CharField(max_length=100)),
                ('appreciation', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('colour', models.CharField(max_length=100)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Minor_Programmer.user_mp')),
            ],
        ),
    ]