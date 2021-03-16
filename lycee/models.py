from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(
    max_length = 50,
    blank = False,
    null = False
  )
  birth_date = models.DateField(
    verbose_name= 'date of birth',
    blank = False,
    null = False
  )
  last_name = models.CharField(
    max_length = 255,
    blank = False,
    null = False,
    help_text = "last name",
    default= '???'
  )
  phone = models.CharField(
    max_length = 10,
    verbose_name = "phone number of student",
    blank = False,
    null = False,
    help_text = "phone number of student",
    default= '0123456789'
  )
  email = models.CharField(
    max_length = 255,
    verbose_name = "email of student",
    blank = False,
    null = False,
    help_text = "email of student",
    default = 'a@a.fr'
  )
  comment = models.CharField(
    max_length = 255,
    verbose_name = "email of student",
    blank = False,
    null = False,
    help_text = "email of student",
    default = 'a@a.fr'
  )

class Cursus(models.Model):
  name = models.CharField(
    max_length = 50,
    blank = False,
    null = True,
    default = 'aucun'
  )
  year_from_bac = models.SmallIntegerField(
    help_text = 'year since the bac',
    verbose_name = 'year',
    blank = False,
    default = 0   
  )
  scholar_year = models.CharField(
    max_length = 9,
    blank = False,
    null = True,
    default= '0000-0001'
  )