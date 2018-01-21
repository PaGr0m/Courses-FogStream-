from django.db import models


class Musician(models.Model):
    name = models.CharField(verbose_name="Исполнитель",
                            max_length=25)
    information = models.TextField(verbose_name="Информация",
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name="Жанр",
                            max_length=25)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(verbose_name="Альбом",
                            max_length=25)

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(verbose_name="Песня",
                            max_length=25)
    lyrics = models.TextField(verbose_name="Текст песни",
                              blank=True,
                              null=True)
    lyrics_ru = models.TextField(verbose_name="Текст песни на русском",
                                 blank=True,
                                 null=True)

    musician = models.ForeignKey("Musician",
                                 verbose_name="Исполнитель",
                                 related_name="musician_songs",
                                 on_delete="CASCADE")
    album = models.ForeignKey("Album",
                              verbose_name="Альбом",
                              related_name="album_songs",
                              on_delete="CASCADE")
    genre = models.ForeignKey("Genre",
                              verbose_name="Жанр",
                              related_name="genre_songs",
                              on_delete="CASCADE")

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.name
