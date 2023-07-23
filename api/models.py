from django.db import models
# Create your models here.
class Diabetes(models.Model):
    pregnancies=models.CharField(max_length=200)
    glucose=models.CharField(max_length=200)
    bloodpressure=models.CharField(max_length=200)
    skinthickness=models.CharField(max_length=200)
    insulin=models.CharField(max_length=200)
    bmi=models.CharField(max_length=200)
    diabetespedigreefunction=models.CharField(max_length=200)
    age=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pregnancies} {self.glucose}'