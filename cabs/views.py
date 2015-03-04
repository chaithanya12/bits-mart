from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import logout
from cabs.models import *
from django.contrib.auth.decorators import login_required
from cabs.views import *
import datetime
from django.utils import timezone
#ask for contact at the very beginning

@login_required
def make_cab_offer(request):
	if request.POST:
		try:
			u = request.user
			destination = request.POST['destination']
			# car = request.POST['car']
			# city = request.POST['city']
			# total_cost = request.POST['total_cost']
			date_of_travel = request.POST['date_of_travel'] #convert into right data type later
			seats = request.POST['seats']
			if 'phone' in request.POST:
				phone = request.POST['phone']
			else:
				phone = None
		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')
		date_of_travel = date_of_travel.replace(" ","")
		date_of_travel = date_of_travel.split('-')
		date_of_travel = [int(x) for x in date_of_travel]
		date_of_travel = datetime.datetime(day=date_of_travel[0],month=date_of_travel[1],year=date_of_travel[2]+2000)
		t = CabOffer(user=u,destination=destination,seats=seats,date_of_travel=date_of_travel,phone=phone)
		t.save()
		# return HttpResponse('{"status":"1","message":"sucess"}')
		context = RequestContext(request)
		message = "Offer added!"
		context_dict = {'message':message}
		return render_to_response('makeoffer.html', context_dict, context)
	else:
		context = RequestContext(request)
		context_dict = {'message':message}
		return render_to_response('makeoffer.html', context_dict, context)

# Create your views here.
@login_required
def disable_cab_offer(request):
	if request.POST:
		try:
			cab_CabOffer_id = request.POST['id']
		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')
		try:
			cab_CabOffer = CabCabOffer.objects.get(id=cab_CabOffer_id)
		except:
			return HttpResponse('{"status":"0","message":"Invalid CabOffer ID"}')
		if request.user == cab_CabOffer.user:
			cab_CabOffer.delete()
			return HttpResponse('{"status":"1","message":"sucess"}')
		else:
			return HttpResponse('{"status":"0","message":"This CabOffer does not belong to you."}')
	else:
		raise Http404



@login_required
def show_CabOffers(request):
	all_CabOffers = CabOffer.objects.all()
	context = RequestContext(request)
	context_dict = {'all_CabOffers':all_CabOffers}
	return render_to_response('see_ad_cab.html', context_dict, context)


@login_required
def search_CabOffers(request):
	all_CabOffers = CabOffer.objects.all()
	if request.POST:
		try:
			destination = request.POST['destination']
		except:
			pass
		try:
			date_of_travel = request.POST['date_of_travel']
		except:
			pass
		if not destination or destination=="":
			context = RequestContext(request)
			context_dict = {'all_CabOffers':all_CabOffers}
			return render_to_response('see_ad_cab.html', context_dict, context) 
		if not date_of_travel:
			all_CabOffers = [x for x in all_CabOffers if x.destination == destination] 
		else:
			date_of_travel = date_of_travel.replace(" ","")
			date_of_travel = date_of_travel.split('-')
			date_of_travel = [int(x) for x in date_of_travel]
			time_of_travel = time_of_travel.split(":")
			time_of_travel = [int(x) for x in time_of_travel]
			time_of_travel = request.POST['time_of_travel']
			date_of_travel = datetime.datetime(day=date_of_travel[0],month=date_of_travel[1],year=date_of_travel[2]+2000,hour=time_of_travel[0],minute=time_of_travel[1])
			date_of_travel = timezone.make_aware(date_of_travel,timezone.get_default_timezone())
			all_CabOffers = [x for x in all_CabOffers if x.destination == destination and abs((x.date_of_travel-date_of_travel).days) <= 2]
		context = RequestContext(request)
		context_dict = {'all_CabOffers':all_CabOffers}
		return render_to_response('see_ad_cab.html', context_dict, context) 
	else:
		context = RequestContext(request)
		context_dict = {'all_CabOffers':all_CabOffers}
		return render_to_response('see_ad_cab.html', context_dict, context)