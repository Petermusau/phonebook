from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    photo=models.ImageField()
    phonenumber=models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:index')


