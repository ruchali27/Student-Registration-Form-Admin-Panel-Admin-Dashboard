from django.db import models

# Create your models here.

# Student Registration form

class StudentDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mob_no = models.IntegerField()
    DOB = models.CharField(max_length=500)
    profile_img = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.name

# Admin Dashboard

class StudentDashboard(models.Model):
    sr_no = models.IntegerField()
    name = models.CharField(max_length=500)
    birthdate = models.DateField(auto_now=False)

    def __str__(self):
        return self.name