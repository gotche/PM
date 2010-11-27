# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from prueba.models import PreTask, PreTaskForm, Task, TaskForm

def details(request):

    form = PreTaskForm()

    template='prueba.html'
    data={'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab1(request):

    p = PreTask.objects.all()

    form = TaskForm()

    template='tab1.html'
    data={'pretask':p,'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab2(request):

    template='tab2.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def pretask_input( request):
    pass

def save(request):
    if request.POST:
        form = PreTaskForm(request.POST)
        if form.is_valid():
            form.save()

    template='salidaprueba.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def save_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    template='salidatask.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))
