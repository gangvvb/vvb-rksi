from django.db import models

class Awards(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    image = models.ImageField('Изображение', upload_to='project/images/')
    description = models.CharField('Описание', max_length=250)
    url = models.URLField('Ссылкa', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Награды'
        verbose_name_plural = 'Награда'


class Team(models.Model):
    team_title = models.CharField('Имя Фамилия', max_length=100)
    team_image = models.ImageField('Изображение', upload_to='project/images/')
    team_description = models.CharField('HardSkills', max_length=50)
    team_url_github = models.URLField('Ссылкa github', blank=True)
    team_url_telegram = models.URLField('Ссылкa telegram', blank=True)
    team_url_vk = models.URLField('Ссылкa vk', blank=True)

    def __str__(self):
        return self.team_title

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Команда'
