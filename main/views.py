from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import logout
from main.models import *
from django.contrib.auth.decorators import login_required
def about(request):

	context = RequestContext(request)
	context_dict = {}
	return render_to_response('about.html', context_dict, context)
def home(request):
	if request.user.is_authenticated():
		context = RequestContext(request)
		context_dict = {}
		return render_to_response('home.html', context_dict, context)
	else:
		context = RequestContext(request)
		context_dict = {}
		return render_to_response('about.html', context_dict, context)
# 
def test(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('test.html', context_dict, context)

def makeoffer(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('makeoffer.html', context_dict, context)


@login_required
def make_offere(request):
	if request.POST:
		try:
			u = request.user
			price = request.POST['price']
			img = request.FILES['img']
			# category = request.POST['category']
			description = request.POST['description']
			name = request.POST['name']
			if 'phone' in request.POST:
				phone = request.POST['phone']
			else:
				phone = None

		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')

		category = Category.objects.get(name='electronics')
		t = Offer(user=u,price=price,img=img,category=category,description=description,name=name,phone=phone)
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


@login_required
def make_offert(request):
	if request.POST:
		try:
			u = request.user
			price = request.POST['price']
			img = request.FILES['img']
			# category = request.POST['category']
			description = request.POST['description']
			name = request.POST['name']
			if 'phone' in request.POST:
				phone = request.POST['phone']
			else:
				phone = None

		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')

		category = Category.objects.get(name='trunks')
		t = Offer(user=u,price=price,img=img,category=category,description=description,name=name,phone=phone)
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
def disable_offer(request):
	if request.POST:
		try:
			offer_id = request.POST['id']
		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')
		try:
			offer = Offer.objects.get(id=cab_offer_id)
		except:
			return HttpResponse('{"status":"0","message":"Invalid offer ID"}')
		if request.user == offer.user:
			offer.delete()
			return HttpResponse('{"status":"1","message":"sucess"}')
		else:
			return HttpResponse('{"status":"0","message":"This offer does not belong to you."}')
	else:
		raise Http404

@login_required
def show_offers(request,category):
	all_offers = Offer.objects.all()
	if category == "trunks":
		hide_search = False
	else:
		hide_search = True
	category = Category.objects.get(name=category)
	all_offers = [x for x in all_offers if x.category==category]
	context = RequestContext(request)
	context_dict = {'all_offers':all_offers,'hide_search':hide_search}
	return render_to_response('see_ad_elec.html', context_dict, context)


@login_required
def search_offers_e(request):
	all_offers = Offer.objects.all()
	category = Category.objects.get(name='electronics')
	all_offers = [x for x in all_offers if x.category==category]
	if request.POST:
		search_term = request.POST['search_term']
		if search_term == '':
			context = RequestContext(request)
			context_dict = {'all_offers':all_offers}
			return render_to_response('see_ad_elec.html', context_dict, context)
		all_offers = [x for x in all_offers if search_term in x.description or search_term in x.name] 
		context = RequestContext(request)
		context_dict = {'all_offers':all_offers}
		return render_to_response('see_ad_elec.html', context_dict, context)
	else:
		context = RequestContext(request)
		context_dict = {'all_offers':all_offers}
		return render_to_response('see_ad_elec.html', context_dict, context)