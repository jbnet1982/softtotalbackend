from django.db import models

class User(models.Model):
    username = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    email = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=50, blank=True)