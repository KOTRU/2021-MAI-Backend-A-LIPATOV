# Generated by Django 3.0 on 2021-12-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileS3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Файл S3',
                'verbose_name_plural': 'Файлы S3',
            },
        ),
    ]
