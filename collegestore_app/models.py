from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
GENDER_CHOICES = [
    ('Female','Female'),
    ('Male','Male'),


]
PURPOSE_CHOICES = [
    ('Enquiry','Enquiry'),
    ('Place Order','Place Order'),
    ('Return','Return'),

]

class Profile(models.Model):
    NAME = models.CharField(max_length=255)
    DOB = models.DateField()
    AGE = models.IntegerField()
    GENDER = models.CharField(max_length=255,choices=GENDER_CHOICES)
    PHONE_NUMBER = models.IntegerField()
    MAIL_ID = models.CharField(max_length=255)
    ADDRESS = models.TextField(max_length=1000)
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE)
    COURSE = models.CharField(max_length=255,default="B.Sc",null=True)
    PURPOSE = models.CharField(max_length=255,choices=PURPOSE_CHOICES)
    MATERIAL = models.CharField(max_length=255)
