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
    ispaid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    
class webhook_logs(models.Model):
    log = models.TextField()
    log_time = models.DateTimeField(auto_now_add=True)