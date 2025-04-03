from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Card(models.Model):
    word = models.CharField(max_length=100, verbose_name="Слово")
    translation = models.CharField(max_length=100, verbose_name="Перевод")
    illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True, verbose_name="Иллюстрация")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cards', verbose_name="Категория")

    def __str__(self):
        return f"{self.word} - {self.translation}"