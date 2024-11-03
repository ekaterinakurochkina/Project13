from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price = models.IntegerField(verbose_name='Цена за покупку', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'