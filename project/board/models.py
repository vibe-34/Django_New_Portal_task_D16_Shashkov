from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .category_type import CATEGORY_TYPE


class Announcement(models.Model):  # Объявление
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст объявления")
    category = models.CharField(max_length=2, choices=CATEGORY_TYPE, default='TN', verbose_name="Категория")
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    upload = models.FileField(upload_to='uploads/', help_text="Загрузите файл", blank=True, verbose_name="Загрузка")

    def __str__(self):
        return f"{self.title} : {self.text} : {self.category}"

    def get_absolute_url(self):
        return f'/announcement/{self.id}'

    # class Meta:
    #     verbose_name = "Объявление"
    #     verbose_name_plural = "Объявления"
    #     ordering = ["-dateCreation"]


class UserResponse(models.Model):  # Отклик
    responder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Откликнувшийся")
    adComment = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name="Комментарий")  # к какому объявлению
    text = models.TextField(verbose_name="Описание")
    # dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата отклика") нет в ТЗ
    status = models.BooleanField(default=False, verbose_name="Статус отклика")

    def __str__(self):
        return f"{self.responder} : {self.text} [:20] + ..."

    def get_absolute_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.adComment.id})

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"
        ordering = ["id"]


# class Subscription(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='subscriptions',
#     )
#     category = models.ForeignKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='subscriptions',
#     )
