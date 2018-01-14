from django.db import models


class Musician(models.Model):
    musician = models.CharField("Исполнитель", max_length=20)

    class Meta:
        ordering = ("musician",)
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.musician


class Genre(models.Model):
    genre = models.CharField("Жанр", max_length=20)

    class Meta:
        ordering = ("genre",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre


class Album(models.Model):
    album = models.CharField("Альбом", max_length=20)

    class Meta:
        ordering = ("album",)
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.album


class Song(models.Model):
    song = models.CharField("Песня", max_length=25)
    lyrics = models.TextField("Текст песни", blank=True, null=True)
    lyrics_ru = models.TextField("Текст песни на русском", blank=True, null=True)

    musician = models.ForeignKey("Musician", verbose_name="Исполнитель", on_delete="CASCADE")
    album = models.ForeignKey("Album", verbose_name="Альбом", on_delete="CASCADE")
    genre = models.ForeignKey("Genre", verbose_name="Жанр", on_delete="CASCADE")

    class Meta:
        ordering = ("musician",)
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return "{}_{}".format(self.musician, self.song)
