from django.db import models

# Create your models here.
class Movie(models.Model):
    Hero_name=models.CharField(max_length=100)
    Heroine_name=models.CharField(max_length=100)
    Director_name=models.CharField(max_length=100)
    Producer_name=models.CharField(max_length=100)
    Year=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.Hero_name