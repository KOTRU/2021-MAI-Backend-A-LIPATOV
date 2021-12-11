from django.db import models
from django.contrib.auth.models import User

class FileS3(models.Model):
    url = models.URLField('Ссылка',null =True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name="owners_file")

    def __str__(self):
        return f"{self.url}"
  
    class Meta:
        verbose_name = "Файл S3"
        verbose_name_plural = "Файлы S3"