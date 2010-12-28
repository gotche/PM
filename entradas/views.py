from django.shortcuts import render_to_response, get_object_or_404
from intranet_dev.entradas.models import Entrada, Empleado
from intranet_dev.login.models import Profile
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django import template
from django.contrib.auth.models import User
import django.core.exceptions
import datetime 

def permiso_de_acceso(user):
    try:
        perfil = user.get_profile()
        #si la ejecucion continua es que tenemos un perfil predefinido
        try:
            perfil.permisos.index('a')
            perfil.permisos.index('b')
            acceso = True
        except ValueError:
            acceso= False

    #except DoesNotExist: La exception debe ser esta pero no soy capaz de localizar donde se encuentra
    except Exception, e:
        #rescatamos la info de permisos del usuario
        try:
            #p = Empleado.objects.get(pk=user.id)
            p = get_object_or_404(Empleado,user=user.id)
        except: 
            #Si no estamos autenticados
            return False
            
        perfil = Profile(user=user,permisos=p.permisos)
        perfil.save()

    try:
        perfil.permisos.index('a')
        perfil.permisos.index('b')
        acceso = True
    except ValueError:
        acceso= False
    return acceso

@login_required
@user_passes_test(permiso_de_acceso, login_url="/")
def details(request):
    p = Entrada.objects.order_by('id').reverse()[:5]
    e = Empleado.objects.all()
    return render_to_response('entradas/destinatarios.html', {'entradas_list': p, 'empleados' : e}, context_instance=template.RequestContext(request))

def guardar (request):
    destinatario = get_object_or_404(Empleado, pk=request.POST['dest'])
    p = Entrada (descripcion = request.POST['descripcion'], destinatario = destinatario, origen = request.POST['origen'])
    p.save()
    mensaje =u"Se ha recibido una entrada a su nombre con los siguientes datos: \n\
              Numero de referencia: %s \n\
              Descripcion: %s \n\
              Destinatario: %s \n\
              Origen:%s \n\
              Fecha de entrada: %s " % ( p.id, p.descripcion,p.destinatario, p.origen, p.creacion.strftime('%d-%m-%Y %H:%M:%S%z'))
    send_mail('Se ha recibido una entrada a su nombre', mensaje, 'entradas@sadesi.es',[destinatario.correo], fail_silently=False)
    return HttpResponseRedirect(reverse('intranet_dev.entradas.views.results', args=(p.id,)))


def results(request, entrada_id):
    p = get_object_or_404(Entrada, pk=entrada_id)
    return render_to_response('entradas/results.html', {'entrada': p},context_instance=template.RequestContext(request))

def details_editar(request, entrada_id):
    p = get_object_or_404(Entrada, pk=entrada_id)
    e = Empleado.objects.all()

    return render_to_response('entradas/entrada_detail.html', {'entrada': p, 'empleados' : e},context_instance=template.RequestContext(request))

def editar (request, entrada_id):
    destinatario = get_object_or_404(Empleado, pk=request.POST['dest'])
    entrada = get_object_or_404(Entrada, pk=entrada_id)

    if entrada.destinatario.id != destinatario.id:
        mensaje_al_error=u'La entrada a la que hacia referencia un correo anterior era erronea'
        send_mail('Entrada erronea', mensaje_al_error, 'entradas@sadesi.es',[entrada.destinatario.correo], fail_silently=False)

    p = Entrada (id= entrada_id,descripcion = request.POST['descripcion'], destinatario = destinatario, origen = request.POST['origen'])
    p.save()
    # en p no se encuentra el attr creacion asi que usamos entrada.creacion
    mensaje =u"Se ha recibido una entrada a su nombre con los siguientes datos: \n\
              Numero de referencia: %s \n\
              Descripcion: %s \n\
              Destinatario: %s \n\
              Origen:%s \n\
              Fecha de entrada: %s " % ( p.id, p.descripcion,p.destinatario, p.origen, entrada.creacion.strftime('%d-%m-%Y %H:%M:%S%z'))
    send_mail('Se ha recibido una entrada a su nombre', mensaje, 'entradas@sadesi.es',[destinatario.correo], fail_silently=False)
    

    return HttpResponseRedirect(reverse('intranet_dev.entradas.views.results', args=(p.id,)))

