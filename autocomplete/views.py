# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from prueba.models import PreTask, PreTaskForm, Task, TaskForm, DetailedTaskForm
from entradas.models import Empleado as Employee
from django.utils import simplejson
from django.http import HttpResponse

def details(request):

    form = TaskForm()

    template='autocomplete.html'
    data={'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def user_lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'term'):
            value = request.GET[u'term']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = Task.objects.filter(title__icontains=value)
                results = [ x.title for x in model_results ]
    json =  simplejson.dumps(results) 
    return HttpResponse(json, mimetype='application/json')

def save(request):

    post = None

    if request.method == "POST":
        print request.POST
        post = request.POST

    template='autocomplete_si.html'
    data={'d':post,}
    return render_to_response(template, data, context_instance=RequestContext(request))
