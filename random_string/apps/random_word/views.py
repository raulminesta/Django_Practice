from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils.crypto import get_random_string
def index(request):
	try:
		request.session['attempt']
	except:
		request.session['attempt'] = 1
	return render(request, 'random_word/index.html')
def randomize(request):
	request.session['mystring'] = get_random_string(length=14)
	request.session['attempt'] += 1
	return redirect('index')