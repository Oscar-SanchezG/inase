# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_doc(request):
    return render(request, 'base/base.html')

def index_his(request):
    return render(request, 'documento/historia.html')

def index_vin(request):
    return render(request, 'documento/vinculacion.html')