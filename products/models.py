from django.db import models

class AuthorBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Raul Larry')

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    objects = models.Manager()
    author_books = AuthorBookManager()
    def __str__(self):
        return self.author +" "+ self.title


