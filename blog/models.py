from django.db import models

from config.settings import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    content = models.TextField(verbose_name="Cодержимое статьи")
    image = models.ImageField(
        upload_to='blog/images/',
        verbose_name="Изображение",
        **NULLABLE,
    )
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return f"Статья блога: {self.title}"


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title", "created_at", "views_count"]

        permissions = [
            ("content_manager", "Контент_менеджер"),
        ]
