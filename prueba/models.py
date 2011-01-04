from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from entradas.models import Empleado as Employee # TODO: translate module entradas source code

class PreTask( models.Model):
    title = models.CharField(max_length=300)

class PreTaskForm( ModelForm):
   class Meta:
        model = PreTask

states_values = (
    ('0','Inbox'),
    ('1','Delayed'),
    ('2','Todo'),
    ('3','Solved'),
    ('4','Rejected'),
    ('5','Re-opened'),
    ('6','Closed'),
)

class Task( models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank =True, default='')
    creator = models.ForeignKey(Employee)
    creation_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=4,choices=states_values,default='0')
    workers = models.ManyToManyField(Employee, related_name='w')


class TaskForm( ModelForm):
   class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            #'description': Textarea (attrs={'rows': 4, 'columns': 100,}),
        }

class DetailedTaskForm(ModelForm):
   class Meta:
        model = Task
        fields = ('title','description','state','creator','workers',)
        widgets = {
            'description': Textarea (attrs={'rows': 4, 'style': 'width:20em;',}),
            #'id': Textarea (attrs={'display': None,}),
            'title': TextInput (attrs={'style':'width:20em;',}),
            'state': TextInput (attrs={'style':'display:none;',}),
            'creator': TextInput (attrs={'style':'display:none;',}),
            'workers': TextInput (attrs={'class':'ui-autocomplete-input', 'type':'text', 'autocomplete':"off", 'role':"textbox", 'aria-autocomplete':"list", 'aria-haspopup':"true",}),
        }

