from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField('Название проекта', max_length=50)
    start_date = models.DateField('Дата начала проекта')
    finish_date = models.DateField('Дата окончания проекта')

    # tasks = models.ManyToManyField('Tasks')

    PROJECT_STATUS = (
        ('Not started', 'Not started'),
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=11, choices=PROJECT_STATUS)  # default='n')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/projects/{self.id}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Tasks(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='task')
    name = models.CharField('Название задания', max_length=50)
    description = models.TextField('Описание задания')
    TASK_STATUS = (
        ('To Do', 'To Do'),
        ('In progress', 'In Progress'),
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=11, choices=TASK_STATUS)  # default='t')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/projects/{self.id}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

