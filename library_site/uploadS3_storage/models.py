from django.db import models

class FileS3(models.Model):
    url = models.URLField('Ссылка',null =True)

    def __str__(self):
        return f"{self.url}"

    class Meta:
        verbose_name = "Файл S3"
        verbose_name_plural = "Файлы S3"