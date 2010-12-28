from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','intranet_dev.entradas.views.details'),
    (r'^(?P<entrada_id>\d+)/$','intranet_dev.entradas.views.details_editar'),
    (r'^guardar/$','intranet_dev.entradas.views.guardar'),
    (r'^(?P<entrada_id>\d+)/results/$','intranet_dev.entradas.views.results'),
    (r'^(?P<entrada_id>\d+)/guardar/$','intranet_dev.entradas.views.editar'),
)
