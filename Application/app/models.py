from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ] 
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Musician(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name='the related album')
    firt_name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

# class Runner(models.Model):
#     MedalType = models.TextChoices("MedalType","GOLD SILVER BRONZE")
#     name = models.CharField(max_length=60)
#     medal = models.CharField(max_length=10, blank=True, choices=MedalType)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)




