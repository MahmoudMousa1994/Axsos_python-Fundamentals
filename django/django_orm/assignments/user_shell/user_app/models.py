from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email_address = models.CharField(max_length= 255)
    age = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def add_user(form_first_name, form_last_name, form_email, form_age):
    User.objects.create(first_name = form_first_name, last_name = form_last_name,email_address= form_email, age = form_age)

    def __str__(self):
        return f"user's fill name is {self.first_name} {self.last_name}"