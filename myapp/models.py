# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


# class Mapp(models.Model):
#     camera_id = models.CharField(max_length=100, primary_key='True')
#     light_id = models.CharField(max_length=100,unique='True')
#     created_on = models.DateTimeField(auto_now_add=True)
#
#
# class Crossing1(models.Model):
#     cam = models.ForeignKey(Mapp)
#     density = models.CharField(max_length=30, default=None)


# class Stray1(models.Model):
#     cam_id = models.ForeignKey(Mapp)
#     stray = models.BooleanField(default=False)

class Mapp(models.Model):
    camera_id = models.CharField(max_length=80, primary_key='True')
    light_id = models.CharField(max_length=100,unique='True')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Crossing1(models.Model):
    cam = models.ForeignKey(Mapp)
    density = models.CharField(max_length=30, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)