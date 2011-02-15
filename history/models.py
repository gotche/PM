# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from prueba.models import Task

class EventType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class History(models.Model):
    event = models.ForeignKey(EventType)
    user = models.ForeignKey(User,related_name='launcher')
    date = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, null=True)
    users_affected = models.ManyToManyField(User,related_name='affected')
    
    def __unicode__(self):
        return self.event.name
