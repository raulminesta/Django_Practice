from django.shortcuts import render
from django.http import HttpResponse, Http404
from apps.interest.models import User, Interest
# Create your views here.
def index(request):
	return render(request,'interest/index.html')
def show(request):
	users = User.objects.all().select_related('Interest')
	context = {
		"users": users,
	}
	return render(request, 'interest/interest.html', context)
def show_user(request, user_id):
	print 'here'
	print user_id
	user = User.objects.filter(id=user_id).select_related('Interest')[0]
	context = {
		"user": user
	}
	return render(request, 'interest/show.html', context)