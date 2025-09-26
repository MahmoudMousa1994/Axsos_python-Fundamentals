from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default='No description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Auther(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="no notes yet")
    books = models.ManyToManyField(Book,related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


