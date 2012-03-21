from django.conf.urls.defaults import *
urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^hijo$', 'hijo',name='hijo'),
    url(r'^include$', 'include',name='include'),
    url(r'^loop$', 'loop',name='loop'),
)
