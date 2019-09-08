from django.db import models
from django.urls import reverse
import uuid


class Author(models.Model):
    name = models.CharField(max_length=50, help_text='Имя')
    surname = models.CharField(max_length=50, help_text='Фамилия')
    patronymic = models.CharField(max_length=50, null=True, blank=True, help_text='Отчество')
    nickname = models.CharField(max_length=50, help_text='Никнейм')

    class Meta:
        ordering = ['name', 'surname', 'patronymic']

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


def directory_path(instance, filename):
    return 'Django_Site/crosswords/' + str(uuid.uuid1()) + '.txt'


class CrosswordBase(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, help_text='Автор')
    name = models.CharField(max_length=50, help_text='Название кроссворда')
    comment = models.TextField(help_text='Комментарий', blank=True)
    file = models.FileField(upload_to=directory_path)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', '-date']

    def get_absolute_url(self):
        return reverse('crosswords', args=[str(self.id)])

    def __str__(self):
        return 'Автор: ' + str(self.author) + ', название: ' + self.name
