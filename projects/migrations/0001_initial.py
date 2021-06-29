# Generated by Django 3.2.4 on 2021-06-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название проекта')),
                ('start_date', models.DateField(verbose_name='Дата начала проекта')),
                ('finish_date', models.DateField(verbose_name='Дата окончания проекта')),
            ],
        ),
    ]
