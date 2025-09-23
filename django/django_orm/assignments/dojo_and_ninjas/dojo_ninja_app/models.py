from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="no description")

def add_dojo(form_dojo_name, form_city, form_state, form_desc):
    Dojo.objects.create(name = form_dojo_name, city = form_city, state = form_state, desc = form_desc)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo,related_name="ninjas", on_delete=models.CASCADE)


def add_ninja(form_ninja_first_name, form_ninja_last_name, form_dojo_to_ninja):
    dojo = Dojo.objects.get(id=form_dojo_to_ninja)
    Ninja.objects.create(first_name = form_ninja_first_name,last_name = form_ninja_last_name,dojo = dojo)
