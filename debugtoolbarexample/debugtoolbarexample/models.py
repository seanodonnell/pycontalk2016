from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)

class Talk(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker)
