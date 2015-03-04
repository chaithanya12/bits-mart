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
from books.models import *
#ask for contact at the very beginning
branch_list = ['PHY','BIO','CS','EEE','BITS','CE','CHE','CHEM','ECON','FIN','GS','HSS','INSTR','IS','MATH','ME','MF','MGTS','PHA']

@login_required
def make_book_offer(request):
	if request.POST:
		try:
			u = request.user
			name= request.POST['name']
			price= int(request.POST['price'])
		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')
		if 'course_code' in request.POST:
			course_code = request.POST['course_code']
		else:
			course_code = None
		if 'branch' in request.POST:
			branch = request.POST['branch']
		else:
			branch = None
		if 'phone' in request.POST:
			phone = request.POST['phone']
		else:
			phone = None

		t = BookOffer(user=u,course_code=course_code,price=price,branch=branch,phone=phone,name=name)
		t.save()
		# return HttpResponse('{"status":"1","message":"sucess"}')
		context = RequestContext(request)
		message = "Offer added!"
		context_dict = {'message':message}
		return render_to_response('makeoffer.html', context_dict, context)
	else:
		return HttpResponseRedirect('/main/makeoffer/') #add template rendering for form 

# Create your views here.
@login_required
def disable_book_offer(request):
	if request.POST:
		try:
			BookOffer_id = request.POST['id']
		except:
			return HttpResponse('{"status":"0","message":"Form data did not validate."}')
		try:
			bok_offer = BookOffer.objects.get(id=BookOffer_id)
		except:
			return HttpResponse('{"status":"0","message":"Invalid BookOffer ID"}')
		if request.user == cab_BookOffer.user:
			book_offer.delete()
			return HttpResponse('{"status":"1","message":"sucess"}')
		else:
			return HttpResponse('{"status":"0","message":"This BookOffer does not belong to you."}')
	else:
		raise Http404



@login_required
def show_BookOffers(request):
	all_BookOffers = BookOffer.objects.all()
	context = RequestContext(request)
	context_dict = {'all_BookOffers':all_BookOffers}
	return render_to_response('see_ad_books.html', context_dict, context)

@login_required
def search_BookOffers(request):
	all_BookOffers = BookOffer.objects.all()
	if request.POST:

		name= request.POST['name']
		course_code = request.POST['course_code']
		branch = request.POST['branch']
		if name != "":
			all_BookOffers = [x for x in all_BookOffers if name in x.name]
		if branch != "Branch":
			all_BookOffers = [x for x in all_BookOffers if branch == x.branch]
		if course_code != "":
			all_BookOffers = [x for x in all_BookOffers if course_code == x.course_code]
		context = RequestContext(request)
		context_dict = {'all_BookOffers':all_BookOffers}
		return render_to_response('see_ad_books.html', context_dict, context) 
	else:
		context = RequestContext(request)
		context_dict = {'all_BookOffers':all_BookOffers}
		return render_to_response('see_ad_books.html', context_dict, context)