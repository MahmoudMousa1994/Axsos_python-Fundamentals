from django.db import models
import datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Shows title should at least 2 characters"
        
        if len(postData['network']) < 3:
            errors["network"] = "Network name should at least 3 characters"
        
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should at least 10 characters"

        if not postData['r_date']:
            errors['r_date'] = "Release date is required"
        else:
            release_date = datetime.datetime.strptime(postData['r_date'], "%Y-%m-%d").date()
            if release_date >= datetime.date.today():
                errors["release_date"] = "Release date should be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(default="no descriptiond")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()