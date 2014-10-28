from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=40)

class Profile(models.Model):
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group)
