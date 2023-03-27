from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        max_length=70,
        unique=True,
        verbose_name='Слаг категории'
    )

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Имя актера'
    )
    surname = models.CharField(
        max_length=70,
        verbose_name='Фамилия актера'
    )
    old = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Возраст актера'
    )
    history = models.TextField(
        verbose_name='История актера'
    )
    photo = models.ImageField(
        upload_to='actors',
        null=True,
        blank=True,
        verbose_name='Фото актера'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Producer(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Имя продюсера'
    )
    surname = models.CharField(
        max_length=70,
        verbose_name='Фамилия продюсера'
    )
    old = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Возраст продюсера'
    )
    history = models.TextField(
        verbose_name='История продюсера'
    )
    photo = models.ImageField(
        upload_to='producers',
        null=True,
        blank=True,
        verbose_name='Фото продюсера'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Жанр',
    )
    description = models.TextField(
        verbose_name='Описание жанра'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Слаг жанра'
    )

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название фильма'
    )
    description = models.TextField(
        verbose_name='Описание фильма'
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актеры фильма',
    )
    image = models.ImageField(
        upload_to='movies',
        null=True,
        blank=True,
        verbose_name='Картинка фильма'
    )
    producer = models.ForeignKey(
        Producer,
        on_delete=models.SET_DEFAULT,
        default='Не задано',
        verbose_name='Продюсер фильма'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр фильма'
    )
    release_date = models.DateTimeField(
        verbose_name='Дата выхода фильма'
    )
    country = models.CharField(
        max_length=70,
        verbose_name='Страна производитель'
    )

    def __str__(self):
        return self.title

