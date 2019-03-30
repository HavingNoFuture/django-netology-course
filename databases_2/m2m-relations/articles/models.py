from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.TextField(null=True, blank=True, verbose_name='Изображение')
    # image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', related_name='articles', through='Relationship')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')


    def __str__(self):
        return self.title


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    main_tag = models.BooleanField(verbose_name='Основной?')
