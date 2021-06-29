# Generated by Django 3.2.4 on 2021-06-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210628_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('Not started', 'Not started'), ('Active', 'Active'), ('Completed', 'Completed')], max_length=11),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('In progress', 'In Progress'), ('Done', 'Done')], max_length=11),
        ),
    ]