# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import insert_registration
# Create your views here.

def registration(request):
	return render(request, 'registration/register.html')

def register(request):
	fname = request.POST['fname']
	lname = request.POST['lname']
	maile = request.POST['Email']
	pwd = request.POST['password']
	bgroup = request.POST['blood_group']
	insert_registration(fname,lname,maile,pwd,bgroup)
	print 'successss'
	return HttpResponse('<h1>Successss')

def index(request):
	return render(request, 'registration/index.html')

def profile(request):
	pass


