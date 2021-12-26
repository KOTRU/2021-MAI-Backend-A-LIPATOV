from django.db import models

def author_directory_path(instance, filename):
    return f'author/{filename}'

class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя автора',max_length=256)
    last_name = models.CharField(verbose_name='Фамилия автора',max_length=256)
    avatar = models.ImageField(verbose_name='Фото автора',upload_to=author_directory_path, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"