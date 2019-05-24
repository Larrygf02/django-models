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

class MaleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='M')

class FemaleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='F')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_OPTIONS = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    )
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS, default=MALE)
    #Managers
    objects = models.Manager()
    males = MaleManager()
    females = FemaleManager()

    #create and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + " "+ self.last_name


