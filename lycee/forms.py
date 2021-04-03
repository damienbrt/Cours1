from django.forms.models import ModelForm
from .models import Student,Presence

class StudentForm(ModelForm):

  class Meta:
     
    #modele
    model = Student
    #les champs qu'on va traiter
    fields =(
      'first_name',
      'last_name',
      'birth_date',
      'email',
      'phone',
      'cursus',
      'comments',
    )

class PresenceForm(ModelForm):

  class Meta:
     
    #modele
    model = Presence
    #les champs qu'on va traiter
    fields =(
      'reason',
      'isMissing',
      'date',
      'time_start',
      'time_end',
      'student',
    )