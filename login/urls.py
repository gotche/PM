from django.conf.urls.defaults import *
#from intranet_dev.entradas.models import Entrada, Empleado

#info_dict = {
#    'queryset': Entrada.objects.all(),
#}

urlpatterns = patterns('',
    (r'','django.contrib.auth.views.login', {'template_name': 'login/login.html'})
)

