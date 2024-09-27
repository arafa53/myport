from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    message=models.TextField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to="port/images")
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    slug=AutoSlugField(populate_from="title",unique=True,null=True,default=None)
