from django.contrib import admin

# Register your models here.
from .models import Student,Cursus

"""
class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "phone", "cursus")
"""

admin.site.register(Student)
admin.site.register(Cursus)

