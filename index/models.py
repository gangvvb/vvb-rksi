from django.db import models


class Articles(models.Model):
    name = models.CharField('Имя', max_length=50)
    full_name = models.CharField('Фамилия', max_length=50)
    course = models.CharField('Курс', max_length=1)
    description = models.TextField('Навыки')
    tel = models.CharField('Телефон', max_length=20)
    url_vk = models.URLField('Ссылкa vk', blank=True)
    gmail = models.CharField('Почта', max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
