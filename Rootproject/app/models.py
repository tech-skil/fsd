from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    description = models.TextField(max_length=500 , blank=True)

    def __str__(self):
        return self.name