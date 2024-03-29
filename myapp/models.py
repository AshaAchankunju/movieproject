from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=200, unique=True)
    language=models.CharField(max_length=200)
    run_time=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    actors=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    managerid=models.IntegerField()
    name=models.CharField(max_length=200, unique=True)
    department=models.CharField(max_length=200)
    salary=models.IntegerField()
    city=models.CharField(max_length=200)

    def __str__(self):
        return self.name

