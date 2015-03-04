from django.conf.urls import patterns, url
from main.views import *

urlpatterns = patterns('',
		url(r'^offers/(?P<category>trunks|electronics)/$',show_offers,name='checkout people'),
		url(r'^electronics/search/$', search_offers_e, name='search electronic stuff'),
		url(r'^makeoffer/$', makeoffer, name='search electronic stuff'),
		url(r'^makeoffere/$', make_offere, name='search electronic stuff'),
		url(r'^makeoffert/$', make_offert, name='search electronic stuff'),
		url(r'^about/$', about, name='search electronic stuff'),

  )
