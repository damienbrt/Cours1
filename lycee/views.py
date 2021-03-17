from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Racine de lycee")

def detail(request, cursus_id):
  resp = 'result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)