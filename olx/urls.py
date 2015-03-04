from django.conf.urls import patterns, include, url
from main.views import *
from django.contrib import admin
from settings import MEDIA_URL, MEDIA_ROOT, DEBUG
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', test ,name='check if client is browser'),
	url(r'^main/', include('main.urls')),
    url(r'^cabs/', include('cabs.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^$', home ,name='check if client is browser'),

)

if DEBUG:
    #urlpatterns=patterns('',url(r'^2014/', include(urlpatterns)))
    from django.views.static import serve
    _media_url = MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': MEDIA_ROOT}))
    del(_media_url, serve)