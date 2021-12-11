from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"