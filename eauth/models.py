from django.db import models

class Signup(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=500, default='')
    dob = models.DateField()
    passphrase = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.full_name

class FileUpload(models.Model):
    file = models.FileField()