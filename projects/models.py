from django.db import models


class Project(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    description = models.CharField('Описания проекта', max_length=250)
    image = models.ImageField('Изображение', upload_to='project/images/')
    url = models.URLField('Ссылкa', blank=True)
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'