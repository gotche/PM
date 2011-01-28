from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$', 'prueba.views.details'),
     (r'^tab1/$', 'prueba.views.tab1'),
     (r'^tab2/$', 'prueba.views.tab2'),
     (r'^tab3/$', 'prueba.views.tab3'),
     (r'^save/$', 'prueba.views.save'),
 
    # tabs2
     (r'^tab21/$', 'prueba.views.tab21'),
     (r'^tab22/$', 'prueba.views.tab22'),
     (r'^tab23/$', 'prueba.views.tab23'),

     (r'^ttask/(?P<state>\d+)/$', 'prueba.views.ttask'),

     (r'^prueba/$', 'prueba.views.prueba'),
     (r'^prueba/save/$', 'prueba.views.pruebasave'),

     #(r'^see_pretask/(?P<id>\d+)$', 'prueba.views.see_pretask'),
     (r'^see_pretask/(?P<task>\d+)$', 'prueba.views.detailed_task'),
     (r'^save_detailed_task/(?P<task_id>\d+)/$', 'prueba.views.save_detailed_task'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
