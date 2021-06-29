# Generated by Django 3.2.4 on 2021-06-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210626_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('n', 'Not started'), ('active', 'Active'), ('c', 'Completed')], default='n', max_length=10),
        ),
    ]
