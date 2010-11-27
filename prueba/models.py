from django.db import models
from django.forms import ModelForm, Textarea

class PreTask( models.Model):
    title = models.CharField(max_length=300)

class PreTaskForm( ModelForm):
   class Meta:
        model = PreTask


class Task( models.Model):
    pre = models.ForeignKey(PreTask)
    desc = models.CharField(max_length=300)

class TaskForm( ModelForm):
   class Meta:
        model = Task
        fields = ('desc',)
        widgets = {
            'desc': Textarea (attrs={'rows': 4, 'columns': 100,}),
        }


