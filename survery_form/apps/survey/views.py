from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def index(request):
	try:
		request.session['count']
	except:
		request.session['count'] =  0
	return render(request,'survey/index.html')
def process_form(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	request.session['count'] += 1
	return redirect('result')
def result(request):
	return render(request,'survey/result.html')