from django.db import models

# Create your models here.

class movies_upload(models.Model):
    language = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='movies/')
    title = models.CharField(max_length=255,null=True)
    movie_type = models.CharField(max_length=255,null=True)

class cinemas_upload(models.Model):
    cinemas_name = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)

class sports_upload(models.Model):
    image = models.ImageField(upload_to='movies/')
    title = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    sports_type = models.CharField(max_length=255,null=True)


class book(models.Model):
    user = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='movies/',null=True)
    title = models.CharField(max_length=255,null=True)
    language = models.CharField(max_length=255,null=True)
    movie_type = models.CharField(max_length=255,null=True)
    cinemas_name = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    sports_type = models.CharField(max_length=255,null=True)
    seats = models.IntegerField(null=True)