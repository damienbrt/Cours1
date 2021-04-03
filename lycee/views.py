from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus,Student,Presence,Appel
from django.template import loader
from django.views.generic.edit import CreateView,UpdateView
from .forms import StudentForm,PresenceForm
from django.urls import reverse
# Create your views here.
"""
def index(request):
  return HttpResponse("Racine de lycee")

def detail(request, cursus_id):
  resp = "result for cursus {}".format(cursus_id)
  return HttpResponse(resp)
"""

def detail(request, cursus_id):
  result_list = Student.objects.all().filter(cursus=cursus_id).order_by('last_name')

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/detail_cursus.html',context)

def detailcall(request, appel_id):
  result_list = Presence.objects.all().filter(appel=appel_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/call/list/detail_call.html',context)

def detailcursuscall(request, cursus_id):
  result_list = Student.objects.all().filter(cursus=cursus_id).order_by('last_name')

  context = {
    'liste' : result_list,
  }

  if request.POST.get("submit") == 'submitSend':
    date = request.POST.get("date")
    time_start = request.POST.get("time_start")
    time_end = request.POST.get("time_end")
    a1 = Appel()
    a1.date = date
    a1.time_start = time_start
    a1.time_end = time_end
    a1.cursus = Cursus.objects.get(id=cursus_id)
    a1.save()
    for student in result_list:
      id = "student"+str(student.id)
      if request.POST.get(id) == "on":
        c1=Presence()
        c1.reason=""
        c1.isMissing = 1
        c1.date = date
        c1.time_start = time_start
        c1.time_end = time_end
        c1.student= Student.objects.get(id=student.id)
        c1.appel = a1
        c1.save()
      else :
        c1=Presence()
        c1.reason=""
        c1.isMissing = 0
        c1.date = date
        c1.time_start = time_start
        c1.time_end = time_end
        c1.student= Student.objects.get(id=student.id)
        c1.appel = a1
        c1.save()
  
  return render(request,'lycee/cursuscall.html',context)

def index(request):
  #result_list = Cursus.objects.all()
  result_list = Cursus.objects.order_by('name')

  #template = loader.get_template('lycee/index.html')
  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/index.html',context)

def indexcall(request):
  #result_list = Cursus.objects.all()
  result_list = Cursus.objects.order_by('name')

  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/call/index.html',context)

def indexcalllist(request):
  #result_list = Cursus.objects.all()
  result_list = Appel.objects.order_by('date')

  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/call/list/index.html',context)

def detail_student(request,student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/student/detail_student.html',context)

def detail_student_call(request,student_id):
  result_list = Presence.objects.all().filter(student=student_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/call/list/student/detail.html',context)

def detail_presence(request,presence_id):
  result_list = Presence.objects.get(pk=presence_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/call/one/detail_presence.html',context)

class StudentCreateView(CreateView):
  #modele
  model = Student
  #formulaire
  form_class = StudentForm
  #template
  template_name = 'lycee/student/create.html'

  def get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))

class StudentUpdateView(UpdateView):
  #modele
  model = Student
  #formulaire
  #template
  template_name = 'lycee/student/edit.html'

  fields = ['first_name','birth_date','last_name','phone','email','comments','cursus']

  def get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))

class PresenceCreateView(CreateView):
  #modele
  model = Presence
  #formulaire
  form_class = PresenceForm
  #template
  template_name = 'lycee/call/one/create.html'
  def get_success_url(self):
    return reverse('detail_presence',args=(self.object.pk,))
