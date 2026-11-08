from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Categorii(models.Model):
    title=models.CharField(max_length=100)
    comment=models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    sale = models.IntegerField()
    material = models.CharField(max_length=100)
    date_prod = models.DateField()
    counter = models.IntegerField()
    cat_id = models.ForeignKey(Categorii, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")




      
# Create your models here.
