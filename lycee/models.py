from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(
    max_lenght = 50,
    blank = False,
    null = False
  )
  birth_date = models.DateField(
    verbose_name= 'date of birth',
    blank = False,
    null = False
  )
  