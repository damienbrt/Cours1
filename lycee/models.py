from django.db import models

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
  def __str__(self):
    return '{} | {}'.format(self.name,self.scholar_year)

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
  comments = models.CharField(
    max_length = 255,
    verbose_name = "comments of student",
    blank = True,
    null = False,
    help_text = "comments of student",
    default = '...'
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete = models.CASCADE,
    null = True
  )
  def __str__(self):
    return '{} {} | {}'.format(self.first_name,self.last_name,self.email)

class Appel(models.Model):
  date = models.DateField(
    verbose_name= 'date',
    blank = False,
    null = False,
    help_text = 'yyyy-mm-ddd'
  )
  time_start = models.TimeField(
    blank=True, 
    null=True,
    help_text = 'HH:MM'
    )
  time_end = models.TimeField(
    blank=True, 
    null=True,
    help_text = 'HH:MM'
    )
  cursus = models.ForeignKey(
    Cursus,
    on_delete = models.CASCADE,
    null = True
  )
  def __str__(self):
    return '{} | {} - {}'.format(self.date,self.time_start ,self.time_end)
    
class Presence(models.Model):
  reason = models.CharField(
    max_length = 50,
    blank = False,
    null = True,
    default = 'aucun'
  )
  isMissing = models.BooleanField(
    verbose_name = 'Is Missing',
    blank = False,
    default = 0   
  )
  date = models.DateField(
    verbose_name= 'date',
    blank = False,
    null = False,
    help_text = 'yyyy-mm-dd',
  )
  time_start = models.TimeField(
    blank=True, 
    null=True,
    help_text = 'HH:MM'
    )
  time_end = models.TimeField(
    blank=True, 
    null=True,
    help_text = 'HH:MM'
    )
  student = models.ForeignKey(
    Student,
    on_delete = models.CASCADE,
    null = True
  )
  appel = models.ForeignKey(
    Appel,
    on_delete = models.CASCADE,
    null = True
  )
  def __str__(self):
    return '{} {} | {} | {}'.format(self.student.first_name,self.student.last_name ,self.isMissing,self.date)
