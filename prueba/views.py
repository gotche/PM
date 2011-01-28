# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from prueba.models import PreTask, PreTaskForm, Task, TaskForm, DetailedTaskForm
from entradas.models import Empleado as Employee

def details(request):

    form = TaskForm()

    template='prueba.html'
    data={'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab1(request):
    # state = 0 (inbox)
    p = Task.objects.filter(state=0)

    p = p.order_by('-id')
    form = TaskForm()

    template='tab1.html'
    data={'pretask':p,'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab2(request):

    template='tab2.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab21(request):

    template='tab21.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab22(request):

    template='tab22.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab23(request):

    template='tab23.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def tab3(request):

    template='tab3.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def ttask(request,state):

    print str(state)
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(state=state)

    template='ttask.html'
    data={'tasks':tasks}
    return render_to_response(template, data, context_instance=RequestContext(request))

def prueba(request):
    # example de ajaxForm
    form = TaskForm()

    template='prue.html'
    data={'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def pruebasave(request):

    # example de ajaxForm
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.creator=Employee.objects.get(user=request.user)
            form.save()
            output = "ok"
    else:
        output = "Post needed"

    data={'output':output,}
    template='salidaprueba.html'
    return render_to_response(template, data, context_instance=RequestContext(request))

def pretask_input( request):
    pass

def detailed_task(request,task):

    t = Task.objects.get(id=task)
    form = DetailedTaskForm(instance=t)

    #print form

    template='see_pretask.html'
    data={'task':t,'form':form,}
    return render_to_response(template, data, context_instance=RequestContext(request))

def save(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.creator=Employee.objects.get(user=request.user)
            t.save()
    template='salidaprueba.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))

def save_detailed_task(request,task_id):

    t = Task.objects.get(pk=task_id)

    if request.POST:

        form = DetailedTaskForm(request.POST,instance=t)

        # which button?
        if "save" in request.POST:

            if request.POST['save'] == "done":
                state = '3'
            if request.POST['save'] == "later":
                state = '2'
            if request.POST['save'] == "idea":
                state = '7'

        print request.POST

        if form.is_valid():
            
            #form.instance.state = state
            #form.instance.creator=Employee.objects.get(user=request.user)
            t = form.save(commit=False)
            t.state=state
            t.save()
            print "form saved"
            print form.instance.state
        else:
            print "no valid"
            print form.errors

    template='salidaprueba.html'
    data={'output': 'ok'}
    return render_to_response(template, data, context_instance=RequestContext(request))

def save_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    template='salidatask.html'
    data={}
    return render_to_response(template, data, context_instance=RequestContext(request))


#def see_pretask(request,id):
#
#    try:
#        pt = Task.objects.get(pk=int(id))
#    except:
#        pt = None
#    
#    template='see_pretask.html'
#    data={'pt':pt,}
#    return render_to_response(template, data, context_instance=RequestContext(request))
