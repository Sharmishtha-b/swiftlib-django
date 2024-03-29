from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    book_issued = models.ForeignKey('books.Book', null=True, on_delete=models.DO_NOTHING)
    pid = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


