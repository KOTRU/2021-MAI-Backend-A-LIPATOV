from django.db import models
from genres.models import Genre
from authors.models import Author

def book_directory_path(instance, filename):
    return f'book/{filename}'

class Book(models.Model):
    title = models.CharField('Название книги',max_length=1024)
    publish_date = models.PositiveSmallIntegerField('Дата публикации')
    rating = models.PositiveSmallIntegerField('Рейтинг')
    cover = models.ImageField('Обложка',upload_to=book_directory_path, null=True, blank=True)
    price = models.PositiveSmallIntegerField('Цена', blank=False)
    genre =  models.ForeignKey(verbose_name='Жанр',to=Genre, on_delete=models.CASCADE, null=True, blank=False, related_name='books')
    author = models.ForeignKey(verbose_name='Автор',to=Author, on_delete=models.CASCADE, null=True, blank=False, related_name='books')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"