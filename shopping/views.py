from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from shopping.models import Product
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib import auth

def index(request):
	products = Product.objects.all()	
	return render_to_response('index.html', locals())

def show(request, resource_id):
	product = Product.objects.get(id=resource_id)
	return render_to_response('show.html', locals())

@login_required
def favorite(request, resource_id):
	return HttpResponse('favorite %s' % resource_id)

def login(request):
	return render_to_response('login.html', locals(), RequestContext(request))

def authenticate(request):
	user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
	if user == None:
		return HttpResponse('username or password error')

	auth.login(request, user)
	return HttpResponseRedirect('/')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')	