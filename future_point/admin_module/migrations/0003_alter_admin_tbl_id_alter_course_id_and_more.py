# Generated by Django 4.0.3 on 2022-04-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0002_auto_20220203_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_tbl',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notification_tbl',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]