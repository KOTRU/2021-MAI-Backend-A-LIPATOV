from django.db import models

def author_directory_path(instance, filename):
    return 'author_{0}/{1}'.format(instance.id, filename)

class Author(models.Model):
    first_name = models.CharField('Имя автора',max_length=256)
    last_name = models.CharField('Фамилия автора',max_length=256)
    avatar = models.ImageField('Фото автора',upload_to=author_directory_path, null=True, blank=True)