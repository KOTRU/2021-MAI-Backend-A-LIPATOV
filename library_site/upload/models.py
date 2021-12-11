from django.db import models

def upload_directory_path(instance, filename):
    return f'upload/{filename}'

class File(models.Model):
    file = models.FileField('Файл',upload_to=upload_directory_path, null=True, blank=True)

    def __str__(self):
        return f"{self.file}"

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"