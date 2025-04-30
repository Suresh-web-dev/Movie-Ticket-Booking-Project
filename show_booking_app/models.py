from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class sign(models.Model):
    username = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    password1 = models.CharField(max_length=255,null=True)
    password2 = models.CharField(max_length=255,null=True)


class log(models.Model):
    username = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)


class image_upload(models.Model):
    language = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255,null=True)
    movie_type = models.CharField(max_length=255,null=True)


class events_upload(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)



class sports_upload(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    sports_type = models.CharField(max_length=255,null=True)



class cinemas_upload(models.Model):
    cinemas_name = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)


class book(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    language = models.CharField(max_length=255,null=True)
    movie_type = models.CharField(max_length=255,null=True)
    cinemas_name = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    sports_type = models.CharField(max_length=255,null=True)
    seats = models.IntegerField(null=True)