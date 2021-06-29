# Generated by Django 3.2.4 on 2021-06-26 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('n', 'Not started'), ('a', 'Active'), ('c', 'Completed')], default='n', max_length=10),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название задания')),
                ('description', models.TextField(verbose_name='Описание задания')),
                ('status', models.CharField(choices=[('t', 'To Do'), ('i', 'In Progress'), ('d', 'Done')], default='t', max_length=10)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects')),
            ],
        ),
    ]
