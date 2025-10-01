from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['cours_name'])<5:
            errors["cours_name"] = "course name ahould be more than 5 characters"
        return errors

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['desc'])< 15:
            errors["desc"] = "course name ahould be more than 15 characters"
        return errors
class Course(models.Model):
    cours_name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    desc = models.TextField(default="no description")
    course = models.OneToOneField(Course, related_name="description", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


