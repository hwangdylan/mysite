from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254) 
    subject = models.TextField(max_length=3000)
    body = models.TextField(max_length=3000)
