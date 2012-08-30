from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index'),
    url(r'^maquinas/$', 'ping.views.index'),
    url(r'^prendidas/$', 'ping.views.prendidas'),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^login/$', 'ping.login.index'),
    #url(r'^ping/(?P<maquina_id>\d+)/$', 'ping.views.detail'),
    #url(r'^ping/(?P<maquina_id>\d+)/results/$', 'ping.views.results'),
    #url(r'^ping/(?P<maquina_id>\d+)/vote/$', 'ping.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
