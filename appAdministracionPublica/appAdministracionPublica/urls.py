from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home/', 'APublica.views.home', name='home'),
     url(r'^hora_actual/', 'APublica.views.hora_actual', name='hora_actual'),
    # url(r'^appAdministracionPublica/', include('appAdministracionPublica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
