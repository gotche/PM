from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$','django.contrib.auth.views.login', {'template_name': 'login/login.html'}),
     (r'^prueba/', include('prueba.urls')),
     (r'^autocomplete/', include('autocomplete.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
     (r'^mymedia/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/gotche/codigo/PM/mymedia/', 'show_indexes': True}),


)
