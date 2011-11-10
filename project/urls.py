from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^user/$', 'version1.views.index'),
    url(r'^user/validatecard/$', 'version1.views.validatecard'),
    url(r'^user/validatepin/$', 'version1.views.validatepin'),
    url(r'^admin/', include(admin.site.urls)),
)
