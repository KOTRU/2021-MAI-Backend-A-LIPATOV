from django.db import models
from genres.models import Genre
from authors.models import Author

def book_directory_path(instance, filename):
    return 'book_{0}/{1}'.format(instance.id, filename)

class Book(models.Model):
    title = models.CharField('Название книги',max_length=1024)
    publish_date = models.PositiveSmallIntegerField('Дата публикации')
    rating = models.PositiveSmallIntegerField('Рейтинг')
    cover = models.ImageField('Обложка',upload_to=book_directory_path, null=True, blank=True)
    capacity = models.PositiveSmallIntegerField('Колличество оставшихся книг')
    price = models.PositiveSmallIntegerField('Цена', blank=False)
    genre =  models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=False, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=False, related_name='books')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"