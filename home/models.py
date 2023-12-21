from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_tittle = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.book_tittle


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
