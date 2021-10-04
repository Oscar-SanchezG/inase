from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_inv(request):
    return render(request,'investigacion/investigaciones.html')

def index_infra(request):
    return render(request,'infraestructura/infraestructura.html')