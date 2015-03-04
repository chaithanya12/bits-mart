from django.conf.urls import patterns, url
from cabs.views import *

urlpatterns = patterns('',

		url(r'^offers/$',show_CabOffers,name='checkout people'),
		url(r'^makeoffer/$',make_cab_offer,name='checkout people'),
		url(r'^search/$',search_CabOffers,name='checkout people'),
  )
