# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def Main(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'base.html')