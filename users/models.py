from django.db import models
from django.utils import timezone
from datetime import timedelta

class InternshipApplication(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    domain = models.CharField(max_length=200)
    college = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    qualification = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    ispaid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Only set the time on creation
            self.time = timezone.now() + timedelta(hours=5, minutes=30)
        super(InternshipApplication, self).save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Only set the time on creation
            self.time = timezone.now() + timedelta(hours=5, minutes=30)
        super(Contact, self).save(*args, **kwargs)

class webhook_logs(models.Model):
    log = models.JSONField()
    log_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Only set the time on creation
            self.log_time = timezone.now() + timedelta(hours=5, minutes=30)
        super(webhook_logs, self).save(*args, **kwargs)