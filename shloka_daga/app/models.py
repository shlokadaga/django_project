from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.