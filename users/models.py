from django.db import models

class InternshipApplication(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    domain = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    qualification = models.CharField(max_length=200)
    year = models.IntegerField()
    source = models.CharField(max_length=200)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()