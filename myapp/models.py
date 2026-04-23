from django.db import models

# Create your models here.
class AppleModel(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    cpass=models.CharField(max_length=10,null=True,blank=True)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.fname

