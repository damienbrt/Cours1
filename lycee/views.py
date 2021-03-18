from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus,Student
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm
from django.urls import reverse

# Create your views here.
"""
def index(request):
  return HttpResponse("Racine de lycee")
"""
def detail(request, cursus_id):
  resp = "result for cursus {}".format(cursus_id)
  return HttpResponse(resp)

def index(request):
  #result_list = Cursus.objects.all()
  result_list = Cursus.objects.order_by('name')

  #template = loader.get_template('lycee/index.html')
  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/index.html',context)

def detail_student(request,student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/student/detail_student.html',context)

class StudentCreateView(CreateView):
  #modele
  model = Student
  #formulaire
  form_class = StudentForm
  #template
  template_name = 'lycee/student/create.html'

  def get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))