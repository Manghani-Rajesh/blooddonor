# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class registration(models.Model):
	firstName = models.CharField(max_length = 200)
	lastName = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	bloodgroup = models.CharField(max_length = 200)

def insert_registration(fname, lname, maile, pwd,bgroup):
	reg = registration(firstName = fname, lastName = lname,
	 email = maile, password = pwd, bloodgroup = bgroup)
	reg.save()