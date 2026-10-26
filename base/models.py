from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()


class CompleteModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

class TrashModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()