from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=95)
    description = models.TextField()
    technology = models.CharField(max_length=120)
    image = models.FilePathField(path="/img")