# Generated by Django 3.2 on 2021-04-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_tb3_nw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneno', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=100)),
                ('gname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('gphno', models.CharField(max_length=100)),
            ],
        ),
    ]