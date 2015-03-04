from django.conf.urls import patterns, url
from books.views import *

urlpatterns = patterns('',

		url(r'^offers/$',show_BookOffers,name='checkout people'),
		url(r'^search/$', search_BookOffers, name='search electronic stuff'),
		url(r'^makeoffer/$', make_book_offer, name='search electronic stuff'),

  )
