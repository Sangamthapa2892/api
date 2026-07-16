from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='students', null=True)
    def __str__(self):
        return self.name
    